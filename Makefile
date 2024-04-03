SETUPPY_VERSION := $(shell grep -P "^__VERSION__" setup.py | awk '{print $$3}' )

develop:
	pip install --editable .
build-clean:
	rm -rf -- ./dist ./build ./**.egg-info ./*.egg-info ./**/__pycache__ ./__pycache__
build-package:
	python3 setup.py sdist bdist
gh-release:
	@bash ./gh-release.sh ${SETUPPY_VERSION}
build: build-clean build-package
release: build gh-release