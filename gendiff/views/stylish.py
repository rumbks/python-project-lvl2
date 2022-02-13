import json
from typing import Dict, Any, Union

from gendiff.types import Node, NodeType

INDENT = "    "


def stringify_value(value: Union[Any, Dict], depth: int) -> str:
    if isinstance(value, Dict):
        result = ["{"]
        for key_, value_ in sorted(value.items()):
            result.append(
                f"{INDENT*(depth+1)}{key_}: {stringify_value(value_, depth+1)}"
            )
        result.append(f"{INDENT*depth}}}")
        return "\n".join(result)
    return value if isinstance(value, str) else json.dumps(value)


def stringify_node(key: str, node: Node, depth: int) -> str:
    if node.type == NodeType.NESTED:
        result = [f"{INDENT*depth}{key}: {{"]
        for key_, node_ in node.value.items():
            result.append(stringify_node(key_, node_, depth + 1))
        result.append(f"{INDENT*depth}}}")

    elif node.type in (
        NodeType.REMOVED,
        NodeType.ADDED,
        NodeType.CHANGED,
        NodeType.UNCHANGED,
    ):
        result = []
        marks = tuple(node.type.value)
        values = node.value if isinstance(node.value, tuple) else (node.value,)
        for mark, value in zip(marks, values):
            result.append(
                f"{INDENT *(depth-1)}  {mark} {key}: "
                f"{stringify_value(value, depth)}"
            )
    else:
        raise RuntimeError(f"Unknown node type: {node.type}")
    return "\n".join(result)


def to_stylish(tree: Dict[str, Node]) -> str:
    result = ["{"]
    for key in tree.keys():
        result.append(stringify_node(key, tree[key], 1))
    result.append("}")
    return "\n".join(result)
