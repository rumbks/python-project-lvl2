import json
from typing import Dict

from gendiff.types import DiffValue

INDENT = 4


def to_json(diff_dict: Dict[str, DiffValue]) -> str:
    return json.dumps(diff_dict, sort_keys=True, indent=INDENT, default=str)
