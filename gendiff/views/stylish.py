import json
from typing import Dict, Any

from gendiff.types import DiffValue, DiffStatus, get_type, ValueType

INDENT = "    "


def _mark_item(item_repr: str, mark: str, depth: int) -> str:
    return "".join(
        [f"{INDENT*(depth-1)}  {mark} ", item_repr[len(INDENT) * depth:]]
    )


def _stylify_scalar(key: str, value: Any, depth: int) -> str:
    value = (
        value if isinstance(value, str) else json.JSONEncoder().encode(value)
    )
    return f"{INDENT*depth}{key}: {value}"


def _stylify_dict(key: str, value: Dict[str, Any], depth: int) -> str:
    result = [f"{INDENT*depth}{key}: {{"]
    for key in sorted(value.keys()):
        result.append(_format[get_type(value[key])](key, value[key], depth + 1))
    result.append(f"{INDENT*depth}}}")
    return "\n".join(result)


def _stylify_diff_value(key: str, value: DiffValue, depth: int) -> str:
    if value.status in (DiffStatus.REMOVED, DiffStatus.ADDED):
        stylified = _format[get_type(value.value)](key, value.value, depth)
        return _mark_item(stylified, value.status.value, depth)

    result = []
    for mark, value_ in zip(("-", "+"), value.value):
        stylified = _format[get_type(value_)](key, value_, depth)
        result.append(_mark_item(stylified, mark, depth))
    return "\n".join(result)


_format = {
    ValueType.SCALAR: _stylify_scalar,
    ValueType.DICT: _stylify_dict,
    ValueType.DIFFVALUE: _stylify_diff_value,
}


def to_stylish(diff_dict: Dict[str, DiffValue]) -> str:
    result = ["{"]
    for key in sorted(diff_dict.keys()):
        result.append(_format[get_type(diff_dict[key])](key, diff_dict[key], 1))
    result.append("}")
    return "\n".join(result)
