# coding: utf-8
#
from setuptools import find_packages, setup

tests_require = ["pytest"]

setup(
    name="human-timedelta",
    version="0.0.1",
    description="Specify Python timedeltas in a human friendly format",
    author="Cosmin Luță",
    author_email="q4break@gmail.com",
    maintainer="Cosmin Luță",
    maintainer_email="q4break@gmail.com",
    packages=find_packages(),
    tests_require=tests_require,
    extras_require={'test': tests_require},
    install_requires=["setuptools"],
)
