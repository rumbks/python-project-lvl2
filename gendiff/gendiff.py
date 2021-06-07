from pathlib import Path
from typing import Dict, Any

from ._diff import DiffValue, get_json_repr_items
from .io import extract_dicts


def _get_json_string_representation(diff_dict: Dict[str, DiffValue]) -> str:
    INDENT = "  "
    result = []
    for key in sorted(diff_dict.keys()):
        result += [
            "".join((INDENT, item))
            for item in get_json_repr_items(key, diff_dict[key])
        ]
    lines = "\n".join(result)
    return f"{{\n{lines}\n}}"


def get_difference_dict(dict1: Dict[str, Any], dict2: Dict[str, any]) -> Dict[str, DiffValue]:
    diff = {}
    for key in dict1:
        if key not in dict2:
            diff[key] = DiffValue(minus=dict1[key])
            continue

        if dict1[key] == dict2[key]:
            diff[key] = DiffValue(unchanged=dict1[key])
        else:
            diff[key] = DiffValue(minus=dict1[key], plus=dict2[key])
        dict2.pop(key)

    for key in dict2:
        diff[key] = DiffValue(plus=dict2[key])
    return diff


def generate_diff(file1: Path, file2: Path) -> str:
    dict1, dict2 = extract_dicts(file1, file2)
    diff = get_difference_dict(dict1, dict2)
    return _get_json_string_representation(diff)
