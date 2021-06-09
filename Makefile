-include Makefile.local

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

reinstall: install build
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest -vv tests

.PHONY: tests