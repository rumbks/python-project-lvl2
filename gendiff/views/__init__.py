from .stylish import to_stylish
from .plain import to_plain
from .json import to_json


STYLISH = "stylish"
PLAIN = "plain"
JSON = "json"

views = {STYLISH: to_stylish, PLAIN: to_plain, JSON: to_json}
