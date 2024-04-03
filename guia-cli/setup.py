import os
from setuptools import setup, find_packages


def iopen(filepath):
    absolute_path_relative_to_setuppy = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        filepath,
    )
    with open(absolute_path_relative_to_setuppy) as f:
        requirements = f.read()


requirements = iopen("requirements.txt").splitlines()
readme_text = iopen("README.md")

# https://packaging.python.org/en/latest/key_projects/#setuptools
setup(
    name="guia_cli",
    version="0.1",
    author="Anderson Bosa",
    description="IA Agent, specializes in software engineering, aiding in coding tasks and providing technical guidance.",
    long_description=readme_text,
    keywords="IA assistant gemini-pro",
    url="https://github.com/andersonbosa/guia-cli",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
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
