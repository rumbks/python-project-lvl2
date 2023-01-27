import json
from typing import Dict, Any
from functools import partial

from gendiff.types import Node, NodeType


filter_unchanged = partial(filter, None)


def stringify_value(value: Any) -> str:
    if isinstance(value, Dict):
        return "[complex value]"
    return f"'{value}'" if isinstance(value, str) else json.dumps(value)


def stringify_node(key_path: str, node: Node) -> str:
    if node.type == NodeType.CHANGED:
        from_, to_ = map(stringify_value, node.value)
        return f"Property '{key_path}' was updated. From {from_} to {to_}"
    elif node.type == NodeType.ADDED:
        return (
            f"Property '{key_path}' was "
            f"added with value: {stringify_value(node.value)}"
        )
    elif node.type == NodeType.REMOVED:
        return f"Property '{key_path}' was removed"
    elif node.type == NodeType.UNCHANGED:
        return ""
    elif node.type == NodeType.NESTED:
        result = []
        for key_, value_ in node.value.items():
            key_path_ = f"{key_path}.{key_}"
            result.append(stringify_node(key_path_, value_))
        return "\n".join(filter_unchanged(result))


def to_plain(tree: Dict[str, Node]) -> str:
    return "\n".join(
        filter_unchanged(
            stringify_node(key, node) for key, node in tree.items()
        )
    )
