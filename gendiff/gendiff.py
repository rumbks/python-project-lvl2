from pathlib import Path

from ._diff import build_difference_dict
from .view import to_stylish
from .io import extract_dicts


def generate_diff(file1: Path, file2: Path) -> str:
    dict1, dict2 = extract_dicts(file1, file2)
    diff = build_difference_dict(dict1, dict2)
    return to_stylish(diff)
