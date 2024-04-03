from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="guia-cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gu = guia-cli.main:main",
            "guia = guia-cli.main:main",
            "gucli = guia-cli.main:main",
        ],
    },
)
