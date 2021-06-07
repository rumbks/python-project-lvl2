import json
from pathlib import Path
from typing import Tuple, Any, Dict, Union, TextIO
import yaml


def get_extension(path: Union[str, Path]) -> str:
    return str(path).split(".")[-1]


def get_dict(file: TextIO, extension: str) -> Dict[str, Any]:
    if extension in ("yml", "yaml"):
        return yaml.load(file) or {}
    if extension == "json":
        return json.load(file)
    raise RuntimeError("Unknown file format")


def extract_dicts(
    path_to_file1: Path, path_to_file2: Path
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    with open(path_to_file1) as file1:
        with open(path_to_file2) as file2:
            dict1 = get_dict(file1, get_extension(path_to_file1))
            dict2 = get_dict(file2, get_extension(path_to_file2))
            return dict1, dict2
