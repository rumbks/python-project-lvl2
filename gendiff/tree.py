from typing import Dict, Any

from gendiff.types import Node, NodeType


def build_difference_tree(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Node]:
    diff = {}
    for key in set(dict1.keys()) - set(dict2.keys()):
        diff[key] = Node(type=NodeType.REMOVED, value=dict1[key])

    for key in set(dict2.keys()) - set(dict1.keys()):
        diff[key] = Node(type=NodeType.ADDED, value=dict2[key])

    for key in set(dict1.keys()) & set(dict2.keys()):
        if dict1[key] == dict2[key]:
            diff[key] = Node(type=NodeType.UNCHANGED, value=dict1[key])
        elif isinstance(dict1[key], Dict) and isinstance(
            dict2[key], Dict
        ):  # noqa: W503
            diff[key] = Node(
                type=NodeType.NESTED,
                value=build_difference_tree(dict1[key], dict2[key]),
            )
        else:
            diff[key] = Node(
                type=NodeType.CHANGED, value=(dict1[key], dict2[key])
            )
    return diff