from pathlib import Path

import pytest
from pytest import fixture

from gendiff import generate_diff

FIXTURES = Path.cwd() / 'tests' / 'fixtures'

JSON1_PATH = FIXTURES / "file1.json"
JSON2_PATH = FIXTURES / "file2.json"
EMPTY_JSON_PATH = FIXTURES / "empty.json"

YAML1_PATH = FIXTURES / "file1.yaml"
YAML2_PATH = FIXTURES / "file2.yaml"
EMPTY_YAML_PATH = FIXTURES / "empty.yaml"


@fixture()
def expected_diff_for_file1_and_file2():
    return """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


@fixture()
def expected_diff_for_file1_and_empty():
    return """{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2", [(JSON1_PATH, JSON2_PATH), (YAML1_PATH, YAML2_PATH)]
)
def test_flat(path_to_file1, path_to_file2, expected_diff_for_file1_and_file2):
    diff = generate_diff(path_to_file1, path_to_file2)
    assert diff == expected_diff_for_file1_and_file2


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2",
    [(JSON1_PATH, EMPTY_JSON_PATH), (YAML1_PATH, EMPTY_YAML_PATH)],
)
def test_flat_file1_and_empty(
    path_to_file1, path_to_file2, expected_diff_for_file1_and_empty
):
    diff = generate_diff(path_to_file1, path_to_file2)
    assert diff == expected_diff_for_file1_and_empty
