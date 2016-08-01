#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Build documentation command module
'''
# Imports

# Package dependencies

from dtb.commands import Command
from dtb.core.constants import BASE_DIR, DATA_DIR, SRC_DIR
from dtb.core.helpers.documentation import ProjectReadme, DatabaseReadme
from dtb.core.helpers.filesystem import File
from dtb.databases import DatabaseRepository

# Classes


class DocumentationBuilderCommand(Command):
    '''The documentation builder command.'''

    @property
    def name(self):
        '''Defines the command name.'''
        return 'build:docs'

    @property
    def description(self):
        '''Defines the command description.'''
        return 'Builds the documentation'

    @property
    def usage(self):
        '''Defines the command usage syntax.'''
        return '%(prog)s'

    def handle(self, args):
        '''Handles the command.'''
        ProjectReadme(File(BASE_DIR / 'README.md'),
                      File(SRC_DIR / 'data/stubs/README.stub.md')) \
            .write()

        for base in DatabaseRepository.listYears():
            # Create raw database READMEs
            DatabaseReadme(File(DATA_DIR / base / 'README.md'),
                           File(SRC_DIR / 'data/stubs/BASE_README.stub.md')) \
                .write()

            # Create minified database READMEs
            DatabaseReadme(File(DATA_DIR / 'minified' / base / 'README.md'),
                           File(SRC_DIR / 'data/stubs/BASE_README.stub.md')) \
                .write()
