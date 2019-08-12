.PHONY: install-dev bump

VERSION=patch

bump:
	bumpversion ${VERSION}

install-dev:
	pip install -e '.[develop]'
