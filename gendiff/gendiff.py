from pathlib import Path

from gendiff.views import views, STYLISH
from .io import load_content
from .parsing import get_extension, parse
from .tree import build_difference_tree


def generate_diff(file1: Path, file2: Path, format: str = STYLISH) -> str:
    file1_content, file2_content = load_content(file1), load_content(file2)
    dict1 = parse(file1_content, get_extension(file1))
    dict2 = parse(file2_content, get_extension(file2))
    diff = build_difference_tree(dict1, dict2)
    return views[format](diff)
