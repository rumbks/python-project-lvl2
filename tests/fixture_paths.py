from pathlib import Path

FIXTURES = Path.cwd() / 'tests' / 'fixtures'
DIFFS = FIXTURES / 'diffs'

JSON1_PATH = FIXTURES / "file1.json"
JSON2_PATH = FIXTURES / "file2.json"
EMPTY_JSON_PATH = FIXTURES / "empty.json"

YAML1_PATH = FIXTURES / "file1.yaml"
YAML2_PATH = FIXTURES / "file2.yaml"
EMPTY_YAML_PATH = FIXTURES / "empty.yaml"

FILE1_FILE2_STYLISH_DIFF = DIFFS / 'file1_file2.stylish.txt'
FILE1_EMPTY_STYLISH_DIFF = DIFFS / 'file1_empty.stylish.txt'

FILE1_FILE2_JSON_DIFF = DIFFS / 'file1_file2.json.txt'
FILE1_EMPTY_JSON_DIFF = DIFFS / 'file1_empty.json.txt'

FILE1_FILE2_PLAIN_DIFF = DIFFS / 'file1_file2.plain.txt'
FILE1_EMPTY_PLAIN_DIFF = DIFFS / 'file1_empty.plain.txt'
