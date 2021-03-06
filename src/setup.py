#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Setup script
'''
# Imports

# Built-in dependencies

import sys

from setuptools import setup, find_packages

# Compatibility check

if sys.version_info[:2] < (2, 7) or (3, 0) <= sys.version_info[:2] < (3, 2):
    raise RuntimeError('Python version 2.7 or >= 3.2 required')

# Routines

setup(
    # Package metadata
    name='dtb',
    version='1.0.0-dev',
    description='Brazilian territorial distribution data exporter',
    license='MIT',
    url='https://github.com/paulofreitas/dtb-ibge',
    author='Paulo Freitas',
    author_email='me@paulofreitas.me',

    # Package distribution
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    entry_points={
        'console_scripts': [
            'dtb = dtb.__main__:main'
        ],
    },

    # Package dependencies
    python_requires='>=2.7,!=3.0.*,!=3.1.*',
    install_requires=[
        # dtb package
        'future',
        # dtb.exporters package
        'fdb',
        'lxml',
        'phpserialize',
        'pyyaml',
        'sqlalchemy',
        # dtb.parsers package
        'xlrd',
    ]
)
