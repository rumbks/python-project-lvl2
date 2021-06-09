from pathlib import Path
from typing import Dict, Any, Union

from .types import DiffValue, get_type, ValueType
from .view import to_stylish
from .io import extract_dicts


def build_difference_dict(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Union[DiffValue, Dict[str, DiffValue], Dict[str, Any]]]:
    diff = {}
    for key in set(dict1.keys()) - set(dict2.keys()):
        diff[key] = DiffValue(minus=dict1[key])

    for key in set(dict2.keys()) - set(dict1.keys()):
        diff[key] = DiffValue(plus=dict2[key])

    for key in set(dict1.keys()) & set(dict2.keys()):
        if dict1[key] == dict2[key]:
            diff[key] = dict1[key]
        elif (
            get_type(dict1[key]) is ValueType.DICT
            and get_type(dict2[key]) is ValueType.DICT
        ):
            diff[key] = build_difference_dict(dict1[key], dict2[key])
        else:
            diff[key] = DiffValue(minus=dict1[key], plus=dict2[key])
    return diff


def generate_diff(file1: Path, file2: Path) -> str:
    dict1, dict2 = extract_dicts(file1, file2)
    diff = build_difference_dict(dict1, dict2)
    return to_stylish(diff)
