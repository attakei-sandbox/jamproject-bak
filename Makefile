.PHONY: install-dev docs lint bump test dist

lint:
	flake8 setup.py src/
	doc8 docs/ specs/

test:
	py.test

docs:
	make -C docs html

VERSION=patch

bump:
	bumpversion ${VERSION}

dist:
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install-dev:
	pip install -e '.[test,docs,develop]'
