from collections import namedtuple
from enum import Enum
from typing import Any, Dict, Union

ValueType = Enum("ValueType", "DICT DIFFVALUE SCALAR")

Nothing = type("Nothing")

DiffValue = namedtuple(
    "DiffValue", ["minus", "plus"], defaults=[Nothing, Nothing]
)


def get_type(value: Any):
    if isinstance(value, DiffValue):
        return ValueType.DIFFVALUE
    elif isinstance(value, Dict):
        return ValueType.DICT
    return ValueType.SCALAR


def build_difference_dict(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Union[DiffValue, Dict[str, DiffValue], Dict[str, Any]]]:
    diff = {}
    for key in dict1:
        if key not in dict2:
            diff[key] = DiffValue(minus=dict1[key])
            continue
        if dict1[key] == dict2[key]:
            diff[key] = dict1[key]
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = build_difference_dict(dict1[key], dict2[key])
        else:
            diff[key] = DiffValue(minus=dict1[key], plus=dict2[key])
        dict2.pop(key)

    for key in dict2:
        diff[key] = DiffValue(plus=dict2[key])
    return diff
