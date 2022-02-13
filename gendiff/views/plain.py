import json
from typing import Dict, Any, Tuple, List, ItemsView

from gendiff.types import Node, NodeType

VALUE = 1


def get_sorted_nodes_with_changes(
    nodes: ItemsView[str, Node]
) -> List[Tuple[str, Node]]:
    return [
        (key, value)
        for (key, value) in sorted(nodes)
        if value.type != NodeType.UNCHANGED
    ]


def stringify_value(value: Any) -> str:
    if isinstance(value, Dict):
        return "[complex value]"
    return (
        f"'{value}'"
        if isinstance(value, str)
        else json.JSONEncoder().encode(value)
    )


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
    elif node.type == NodeType.NESTED:
        result = []
        for key_, value_ in get_sorted_nodes_with_changes(node.value.items()):
            key_path_ = ".".join((key_path, key_))
            result.append(stringify_node(key_path_, value_))
        return "\n".join(result)


def to_plain(diff_dict: Dict[str, Node]) -> str:
    return "\n".join(
        [
            stringify_node(key, value)
            for key, value in get_sorted_nodes_with_changes(diff_dict.items())
        ]
    )
