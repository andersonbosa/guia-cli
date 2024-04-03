from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="guia_cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gu = guia_cli.main:main",
            "guia = guia_cli.main:main",
            "gucli = guia_cli.main:main",
        ],
    },
)
