import pytest
from pytest import fixture

from functools import partial
from gendiff import generate_diff
from tests.fixture_paths import *

generate_diff = partial(generate_diff, format="plain")


@fixture()
def expected_diff_for_file1_and_file2():
    return """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


@fixture()
def expected_diff_for_file1_and_empty():
    return """Property 'common' was removed
Property 'group1' was removed
Property 'group2' was removed"""


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
