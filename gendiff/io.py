import json
from pathlib import Path
from typing import Any, Dict, Union

import yaml


def get_extension(path: Union[str, Path]) -> str:
    return str(path).split(".")[-1]


def parse_data(data: str, extension: str) -> Dict[str, Any]:
    if extension in ("yml", "yaml"):
        return yaml.load(data) or {}
    if extension == "json":
        return json.loads(data)
    raise RuntimeError("Unknown file format")


def load_data(
    path_to_file: Path
) -> str:
    with open(path_to_file) as file:
        return file.read()
