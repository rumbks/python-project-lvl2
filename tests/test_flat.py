import json
from pathlib import Path

from pytest import fixture
from gendiff import generate_diff

FIXTURES = Path.cwd() / 'tests' / 'fixtures'

JSON1_PATH = FIXTURES / 'file1.json'


JSON2_PATH = FIXTURES / 'file2.json'


@fixture
def expected_diff():
    return """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_flat(expected_diff):
    diff = generate_diff(JSON1_PATH, JSON2_PATH)
    assert diff == expected_diff

