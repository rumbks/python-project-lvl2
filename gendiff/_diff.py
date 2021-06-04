from collections import namedtuple
from typing import Dict, Any, List
import json

DiffValue = namedtuple(
    "DiffValue", ["unchanged", "minus", "plus"], defaults=[None, None, None]
)


def to_json_repr_items(key: str, value: DiffValue) -> List[str]:
    def encode(item: Any):
        if isinstance(item, str):
            return item
        return json.JSONEncoder().encode(item)

    result = []
    if value.unchanged is not None:
        result.append(f"  {key}: {encode(value.unchanged)}")
        return result

    if value.minus is not None:
        result.append(f"- {key}: {encode(value.minus)}")

    if value.plus is not None:
        result.append(f"+ {key}: {encode(value.plus)}")

    return result
