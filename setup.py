#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re
import os


def get_version():
    with open(os.path.join(os.path.dirname(__file__), "apts", "__init__.py")) as f:
        match = re.search(r"__version__ = [\'\"]([^\'\"]+)[\'\"]", f.read())
        if match:
            return match.group(1)
    return "0.0.0"


# long_description = read('README.txt', 'CHANGES.txt')

setup(
    name="apts",
    version=get_version(),
    url="http://github.com/pozar87/apts/",
    license="Apache Software License",
    author="Lukasz Pozarlik",
    tests_require=["pytest"],
    install_requires=[
        "aenum>=2.0.6",
        "ephem>=3.7.6.0",
        "skyfield",
        "scipy>=1.0.0",
        "matplotlib>=2.1.2",
        "numpy>=1.14.0",
        "pandas>=0.22.0",
        "pint>=0.8.1",
        "pycairo>=1.16.2",
        "python-igraph>=0.7.1.post6",
        "requests-cache>=1.2.0",
        "requests-mock>=1.12.1",
        "seaborn>=0.8.1",
        "Babel>=2.9.1",
        "svgwrite>=1.1.12",
        "timezonefinder>=2.1.0",
        "pytz>=2018.3",
    ],
    # cmdclass={'test': PyTest},
    author_email="lpozarlik@gmail.com",
    description="Set of tools for automatic astrofotography images aqquisition and processing.",
    # long_description=long_description,
    packages=find_packages(),
    package_dir={"apts": "apts"},
    package_data={"apts": ["data/*", "templates/*", "locale/pl/LC_MESSAGES/*.mo"]},
    include_package_data=True,
    platforms="any",
    # test_suite='sandman.test.test_sandman',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    extras_require={
        "testing": ["pytest", "requests-mock>=1.12.1"],
    },
)
