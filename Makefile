run:
	./.venv/bin/python main.py
build-clean:
	rm -rf -- ./dist
build-package:
	python3 setup.py sdist bdist
gh-release:
	bash ./gh-release.sh
release: build-clean build-package gh-release