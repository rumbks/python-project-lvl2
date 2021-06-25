from pathlib import Path


def load_content(
    path_to_file: Path
) -> str:
    with open(path_to_file) as file:
        return file.read()
