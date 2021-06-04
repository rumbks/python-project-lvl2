import json
from collections import defaultdict
from pathlib import Path
from typing import MutableMapping


def _get_string_representation(diff_dict: MutableMapping[str, str]) -> str:
    result = []
    for key in sorted(diff_dict.keys()):
        result += [f"  {item}" for item in diff_dict[key]]
    lines = '\n'.join(result)
    return f"{{\n{lines}\n}}"


def generate_diff(file1: Path, file2: Path) -> str:
    diff = defaultdict(list)
    json1: dict = json.load(open(file1))
    json2: dict = json.load(open(file2))
    for key in json1:
        if key in json2:
            if json1[key] == json2[key]:
                diff[key] += [f"  {key}: {json1[key]}"]
            else:
                diff[key] += [
                    f"- {key}: {json1[key]}",
                    f"+ {key}: {json2[key]}",
                ]
            json2.pop(key)
            continue
        diff[key] += [f"- {key}: {json1[key]}"]

    for key in json2:
        diff[key] += [f"+ {key}: {json2[key]}"]

    return _get_string_representation(diff)
