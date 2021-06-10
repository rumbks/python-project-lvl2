import pytest
from pytest import fixture

from gendiff import generate_diff
from tests.fixture_paths import *


@fixture()
def expected_diff_for_file1_and_file2():
    return """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


@fixture()
def expected_diff_for_file1_and_empty():
    return """{
  - common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow: 
            }
            key: value
        }
    }
  - group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}"""


@pytest.mark.parametrize(
    "path_to_file1,path_to_file2", [(JSON1_PATH, JSON2_PATH), (YAML1_PATH, YAML2_PATH)]
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
