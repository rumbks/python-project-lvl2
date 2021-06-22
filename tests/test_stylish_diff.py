import pytest
from pytest import fixture

from gendiff import generate_diff
from tests.fixture_paths import (
    JSON1_PATH,
    JSON2_PATH,
    YAML1_PATH,
    YAML2_PATH,
    EMPTY_YAML_PATH,
    EMPTY_JSON_PATH,
    FILE1_FILE2_STYLISH_DIFF,
    FILE1_EMPTY_STYLISH_DIFF,
)


@fixture()
def expected_diff_for_file1_and_file2():
    with FILE1_FILE2_STYLISH_DIFF.open('r') as f:
        yield f.read()


@fixture()
def expected_diff_for_file1_and_empty():
    with FILE1_EMPTY_STYLISH_DIFF.open('r') as f:
        yield f.read()


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2",
    [(JSON1_PATH, JSON2_PATH), (YAML1_PATH, YAML2_PATH)],
)
def test_gendiff_file1_and_file2(
    path_to_file1, path_to_file2, expected_diff_for_file1_and_file2
):
    diff = generate_diff(path_to_file1, path_to_file2)
    assert diff == expected_diff_for_file1_and_file2


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2",
    [(JSON1_PATH, EMPTY_JSON_PATH), (YAML1_PATH, EMPTY_YAML_PATH)],
)
def test_gendiff_file1_and_empty(
    path_to_file1, path_to_file2, expected_diff_for_file1_and_empty
):
    diff = generate_diff(path_to_file1, path_to_file2)
    assert diff == expected_diff_for_file1_and_empty
