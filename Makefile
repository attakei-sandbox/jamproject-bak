.PHONY: install-dev lint bump

lint:
	flake8 setup.py src/

VERSION=patch

bump:
	bumpversion ${VERSION}

install-dev:
	pip install -e '.[test,develop]'
