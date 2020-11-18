.PHONY: test lint black build publish

default: lint

test:
	poetry run coverage run --branch -m pytest -o junit_family=xunit2 --junitxml=junit/test-results.xml -v

lint: pyright black

pyright:
	poetry run pyright --verbose

black:
	poetry run black --check --diff --color .

build:
	poetry build

publish:
	poetry publish
