from collections import namedtuple
from enum import Enum
from typing import Any, Dict


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

