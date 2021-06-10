from .stylish import to_stylish
from .plain import to_plain


STYLISH = "stylish"
PLAIN = "plain"

views = {STYLISH: to_stylish, PLAIN: to_plain}
