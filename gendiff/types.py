from enum import Enum
from typing import Any, NamedTuple, Union, Tuple


DiffStatus = Enum(
    "DiffStatus",
    [
        ("REMOVED", "-"),
        ("ADDED", "+"),
        ("CHANGED", "-+"),
        ("UNCHANGED", " "),
        ("NESTED", "{}"),
    ],
)


DiffValue = NamedTuple(
    "DiffValue",
    [("status", DiffStatus), ("value", Union[Any, Tuple[Any, Any]])],
)
