#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os


def get_version():
    with open(os.path.join(os.path.dirname(__file__), "apts", "__init__.py")) as f:
        return re.search(r"__version__ = [\'\"]([^\'\"]+)[\'\"]", f.read()).group(1)


# long_description = read('README.txt', 'CHANGES.txt')

setup(
    name="apts",
    version=get_version(),
    url="http://github.com/pozar87/apts/",
    license="Apache Software License",
    author="Lukasz Pozarlik",
    tests_require=["pytest"],
    install_requires=[
        "aenum",
        "ephem",
        "skyfield",
        "scipy",
        "matplotlib",
        "numpy",
        "pandas",
        "pint",
        "pycairo",
        "python-igraph",
        "requests-cache",
        "requests-mock",
        "seaborn",
        "Babel",
        "svgwrite",
        "timezonefinder",
        "pytz",
    ],
    # cmdclass={'test': PyTest},
    author_email="lpozarlik@gmail.com",
    description="Set of tools for automatic astrofotography images aqquisition and processing.",
    # long_description=long_description,
    packages=[
        "apts",
        "apts.opticalequipment",
        "apts.objects",
        "apts.constants",
        "apts.utils",
    ],
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
