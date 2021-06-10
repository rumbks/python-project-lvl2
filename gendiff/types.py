from enum import Enum
from typing import Any, Dict, NamedTuple, Union, Tuple

ValueType = Enum("ValueType", "DICT DIFFVALUE SCALAR")


DiffStatus = Enum(
    "DiffStatus",
    [("REMOVED", "-"), ("ADDED", "+"), ("CHANGED", "-+")],
)


DiffValue = NamedTuple(
    "DiffValue",
    [("status", DiffStatus), ("value", Union[Any, Tuple[Any, Any]])],
)


def get_type(value: Any):
    if isinstance(value, DiffValue):
        return ValueType.DIFFVALUE
    elif isinstance(value, Dict):
        return ValueType.DICT
    return ValueType.SCALAR
