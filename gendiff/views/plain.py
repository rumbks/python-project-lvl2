import json
from typing import Dict, Any, Tuple, Iterable

from gendiff.types import Node, NodeType

NODE = 1


def filter_unchanged_nodes(
    key_node_pairs: Iterable[Tuple[str, Node]]
) -> Iterable[Tuple[str, Node]]:
    return filter(
        lambda key_node_pair: key_node_pair[NODE].type != NodeType.UNCHANGED,
        key_node_pairs,
    )


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
    elif node.type == NodeType.NESTED:
        result = []
        for key_, value_ in filter_unchanged_nodes(node.value.items()):
            key_path_ = f"{key_path}.{key_}"
            result.append(stringify_node(key_path_, value_))
        return "\n".join(result)


def to_plain(tree: Dict[str, Node]) -> str:
    return "\n".join(
        stringify_node(key, node)
        for key, node in filter_unchanged_nodes(tree.items())
    )
