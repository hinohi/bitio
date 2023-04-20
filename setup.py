# -*- coding: utf-8 -*-
#
# setup.py
#
from setuptools import setup

setup(
    name="bitio",
    packages=["bitio"],
    version="0.2.0",
    description="Input/output utilities of a bit-basis file",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Daiju Nakayama",
    author_email="42.daiju@gmail.com",
    url="https://github.com/hinohi/bitio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ]
)
