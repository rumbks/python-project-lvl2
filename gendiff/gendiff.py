from pathlib import Path
from typing import Dict, Any

from gendiff.views import views, STYLISH
from .io import load_content
from .parsing import get_extension, parse
from .types import DiffValue, DiffStatus


def build_difference_dict(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, DiffValue]:
    diff = {}
    for key in set(dict1.keys()) - set(dict2.keys()):
        diff[key] = DiffValue(status=DiffStatus.REMOVED, value=dict1[key])

    for key in set(dict2.keys()) - set(dict1.keys()):
        diff[key] = DiffValue(status=DiffStatus.ADDED, value=dict2[key])

    for key in set(dict1.keys()) & set(dict2.keys()):
        if dict1[key] == dict2[key]:
            diff[key] = DiffValue(status=DiffStatus.UNCHANGED, value=dict1[key])
        elif isinstance(dict1[key], Dict) and isinstance(
            dict2[key], Dict
        ):  # noqa: W503
            diff[key] = DiffValue(
                status=DiffStatus.NESTED,
                value=build_difference_dict(dict1[key], dict2[key]),
            )
        else:
            diff[key] = DiffValue(
                status=DiffStatus.CHANGED, value=(dict1[key], dict2[key])
            )
    return diff


def generate_diff(file1: Path, file2: Path, format: str = STYLISH) -> str:
    file1_content, file2_content = load_content(file1), load_content(file2)
    dict1 = parse(file1_content, get_extension(file1))
    dict2 = parse(file2_content, get_extension(file2))
    diff = build_difference_dict(dict1, dict2)
    return views[format](diff)
