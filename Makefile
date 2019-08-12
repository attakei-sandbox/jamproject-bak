.PHONY: install-dev docs lint bump

lint:
	flake8 setup.py src/
	doc8 docs/ specs/

docs:
	make -C docs html

VERSION=patch

bump:
	bumpversion ${VERSION}

install-dev:
	pip install -e '.[test,docs,develop]'
