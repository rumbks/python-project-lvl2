from enum import Enum
from typing import Any, NamedTuple, Union, Tuple


NodeType = Enum(
    "NodeType",
    [
        ("REMOVED", "-"),
        ("ADDED", "+"),
        ("CHANGED", "-+"),
        ("UNCHANGED", " "),
        ("NESTED", "{}"),
    ],
)


Node = NamedTuple(
    "Node",
    [("type", NodeType), ("value", Union[Any, Tuple[Any, Any]])],
)
