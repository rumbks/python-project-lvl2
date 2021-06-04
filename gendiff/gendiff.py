import json
from pathlib import Path
from typing import Dict

from ._diff import DiffValue, to_json_repr_items


def _get_json_string_representation(diff_dict: Dict[str, DiffValue]) -> str:
    INDENT = "  "
    result = []
    for key in sorted(diff_dict.keys()):
        result += [
            "".join((INDENT, item)) for item in to_json_repr_items(key, diff_dict[key])
        ]
    lines = "\n".join(result)
    return f"{{\n{lines}\n}}"


def generate_diff(file1: Path, file2: Path) -> str:
    diff = {}
    json1: dict = json.load(open(file1))
    json2: dict = json.load(open(file2))
    for key in json1:
        if key in json2:
            if json1[key] == json2[key]:
                diff[key] = DiffValue(unchanged=json1[key])
            else:
                diff[key] = DiffValue(minus=json1[key], plus=json2[key])
            json2.pop(key)
            continue
        diff[key] = DiffValue(minus=json1[key])

    for key in json2:
        diff[key] = DiffValue(plus=json2[key])

    return _get_json_string_representation(diff)
