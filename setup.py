#!/usr/bin/env python2
import sys
from setuptools import setup

installs = [
    "requests",
    "beautifulsoup4"
]

setup(
    name="html scraper",
    install_requires=installs,
    url="",
    description="",
    version="1.0.0",
    author="snozaki",
    license="Apache License 2.0",
    entry_points={
        "console_scripts": [
            "scraper = main:Main.printHtmlTitle"
        ]
    }
)