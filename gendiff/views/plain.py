import json
from typing import Dict, Any, Tuple, List

from gendiff.types import DiffValue, DiffStatus, get_type, ValueType

KEY = 0


def sorted_items(dict_: Dict) -> List[Tuple[str, Any]]:
    return sorted([item for item in dict_.items()], key=lambda item: item[KEY])


def simplify_value(value: Any) -> str:
    if isinstance(value, Dict):
        return "[complex value]"
    return (
        f"'{value}'"
        if isinstance(value, str)
        else json.JSONEncoder().encode(value)
    )


def diffvalue_repr(key_path: str, value: DiffValue) -> str:
    if value.status == DiffStatus.CHANGED:
        from_, to_ = map(simplify_value, value.value)
        return f"Property '{key_path}' was updated. From {from_} to {to_}"
    elif value.status == DiffStatus.ADDED:
        return f"Property '{key_path}' was added with value: {simplify_value(value)}"
    elif value.status == DiffStatus.REMOVED:
        return f"Property '{key_path}' was removed"


def next_layer(layer: List[Tuple[str, Any]]) -> List[Tuple[str, Any]]:
    next_ = []
    for _, value in layer:
        if get_type(value) == ValueType.DICT:
            next_ += sorted_items(value)
    return next_


def to_plain(diff_dict: Dict[str, DiffValue]) -> str:
    result = []
    layer_items = sorted_items(diff_dict)
    while layer_items:
        for key_path, value in layer_items:
            if get_type(value) == ValueType.DIFFVALUE:
                result.append(diffvalue_repr(key_path, value))
        layer_items = next_layer(layer_items)
    return "\n".join(result)
