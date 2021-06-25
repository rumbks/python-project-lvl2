from itertools import repeat, cycle

import pytest

from gendiff import generate_diff
from gendiff.views import STYLISH, PLAIN, JSON
from tests.fixture_paths import (
    JSON1_PATH,
    JSON2_PATH,
    YAML1_PATH,
    YAML2_PATH,
    EMPTY_YAML_PATH,
    EMPTY_JSON_PATH,
    FILE1_FILE2_STYLISH_DIFF,
    FILE1_EMPTY_STYLISH_DIFF,
    FILE1_FILE2_PLAIN_DIFF,
    FILE1_EMPTY_PLAIN_DIFF,
    FILE1_FILE2_JSON_DIFF,
    FILE1_EMPTY_JSON_DIFF,
)


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2,path_to_diff,format",
    [
        (path_to_file1, path_to_file2, path_to_diff, format)
        for (path_to_file1, path_to_file2, path_to_diff, format) in zip(
            cycle((JSON1_PATH, YAML1_PATH)),
            cycle((JSON2_PATH, YAML2_PATH, EMPTY_JSON_PATH, EMPTY_YAML_PATH)),
            [
                *repeat(FILE1_FILE2_STYLISH_DIFF, 2),
                *repeat(FILE1_EMPTY_STYLISH_DIFF, 2),
                *repeat(FILE1_FILE2_PLAIN_DIFF, 2),
                *repeat(FILE1_EMPTY_PLAIN_DIFF, 2),
                *repeat(FILE1_FILE2_JSON_DIFF, 2),
                *repeat(FILE1_EMPTY_JSON_DIFF, 2),
            ],
            cycle([*repeat(STYLISH, 4), *repeat(PLAIN, 4), *repeat(JSON, 4)]),
        )
    ],
)
def test_generate_diff(path_to_file1, path_to_file2, path_to_diff, format):
    with open(path_to_diff) as f:
        expected_diff = f.read()
    diff = generate_diff(path_to_file1, path_to_file2, format)
    assert diff == expected_diff
