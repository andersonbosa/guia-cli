SETUPPY_VERSION := $(shell grep -P "^__VERSION__" setup.py | awk '{print $$3}' )

run:
	./.venv/bin/python main.py
build-clean:
	rm -rf -- ./dist
build-package:
	python3 setup.py sdist bdist
gh-release:
	@bash ./gh-release.sh ${SETUPPY_VERSION}
release: build-clean build-package gh-release