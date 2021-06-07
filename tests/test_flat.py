import json
from io import StringIO
from pathlib import Path

from pytest import fixture
from gendiff import generate_diff

FIXTURES = Path.cwd() / 'tests' / 'fixtures'

JSON1_PATH = FIXTURES / 'file1.json'


JSON2_PATH = FIXTURES / 'file2.json'

EMPTY_JSON_PATH = FIXTURES / 'empty.json'


@fixture()
def expected_diff_for_json1_and_json2():
    return """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


@fixture()
def expected_diff_for_json1_and_empty():
    return """{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""


def test_flat(expected_diff_for_json1_and_json2):
    diff = generate_diff(JSON1_PATH, JSON2_PATH)
    assert diff == expected_diff_for_json1_and_json2


def test_flat_json1_and_empty(expected_diff_for_json1_and_empty):
    diff = generate_diff(JSON1_PATH, EMPTY_JSON_PATH)
    assert diff == expected_diff_for_json1_and_empty
