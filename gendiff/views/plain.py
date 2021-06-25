import json
from typing import Dict, Any

from gendiff.types import DiffValue, DiffStatus


VALUE = 1


def stringify_value(value: Any) -> str:
    if isinstance(value, Dict):
        return "[complex value]"
    return (
        f"'{value}'"
        if isinstance(value, str)
        else json.JSONEncoder().encode(value)
    )


def stringify_node(key_path: str, value: DiffValue) -> str:
    if value.status == DiffStatus.CHANGED:
        from_, to_ = map(stringify_value, value.value)
        return f"Property '{key_path}' was updated. From {from_} to {to_}"
    elif value.status == DiffStatus.ADDED:
        return (
            f"Property '{key_path}' was "
            f"added with value: {stringify_value(value.value)}"
        )
    elif value.status == DiffStatus.REMOVED:
        return f"Property '{key_path}' was removed"
    elif value.status == DiffStatus.NESTED:
        result = []
        for key_, value_ in filter(
            lambda item: item[VALUE].status != DiffStatus.UNCHANGED,
            sorted(value.value.items()),
        ):
            key_path_ = ".".join((key_path, key_))
            result.append(stringify_node(key_path_, value_))
        return "\n".join(result)


def to_plain(diff_dict: Dict[str, DiffValue]) -> str:
    return "\n".join(
        [stringify_node(key, value) for key, value in sorted(diff_dict.items())]
    )
