import json
from typing import Dict

from gendiff.types import Node

INDENT = 4


def to_json(tree: Dict[str, Node]) -> str:
    return json.dumps(tree, sort_keys=True, indent=INDENT, default=str)
