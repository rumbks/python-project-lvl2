from typing import Dict, Any

from gendiff.types import Node, NodeType


def build_difference_tree(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Node]:
    diff = {}
    all_keys = dict1.keys() | dict2.keys()

    for key in sorted(all_keys):
        if key not in dict2:
            diff[key] = Node(type=NodeType.REMOVED, value=dict1[key])

        elif key not in dict1:
            diff[key] = Node(type=NodeType.ADDED, value=dict2[key])

        elif dict1[key] == dict2[key]:
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