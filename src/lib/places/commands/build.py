#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Build command module
'''
# Imports

# Package dependencies

from places.commands import Command
from places.core.constants import DATA_DIR
from places.core.logging import Logger
from places.databases import DatabaseFactory, DatabaseRepository
from places.formats import FormatRepository

# Module logging

logger = Logger.instance(__name__)

# Classes


class DatasetBuilderCommand(Command):
    '''
    The dataset builder command.
    '''

    @property
    def name(self):
        '''
        Defines the command name.
        '''
        return 'build'

    @property
    def description(self):
        '''
        Defines the command description.
        '''
        return 'Builds a dataset'

    @property
    def usage(self):
        '''
        Defines the command usage syntax.
        '''
        return '%(prog)s -d DATASET -r FORMAT -m FORMAT'

    def configure(self):
        '''
        Defines the command arguments.
        '''
        datasets = DatabaseRepository.listYears()
        raw_formats = FormatRepository.listExportableFormatNames()
        minifiable_formats = FormatRepository.listMinifiableFormatNames()

        self.addArgument('-d', '--datasets',
                         metavar='DATASET',
                         nargs='*',
                         default=datasets,
                         help=('Datasets to build.\n'
                               'Defaults to all available: {}' \
                                   .format(', '.join(datasets))))
        self.addArgument('-r', '--raw',
                         metavar='FORMAT',
                         nargs='*',
                         default=raw_formats,
                         help=('Raw formats to build the dataset.\n'
                               'Defaults to all available: {}' \
                                    .format(', '.join(raw_formats))))
        self.addArgument('-m', '--min',
                         metavar='FORMAT',
                         nargs='*',
                         default=minifiable_formats,
                         help=('Minifiable formats to build the dataset.\n'
                               'Defaults to all available: {}' \
                                   .format(', '.join(minifiable_formats))))

    def handle(self, args):
        '''
        Handles the command.
        '''
        try:
            for dataset in args.datasets:
                raw_dir = DATA_DIR / dataset
                minified_dir = DATA_DIR / dataset / 'minified'

                logger.info('> Building %s dataset...', dataset)

                raw_dir.create(parents=True)
                minified_dir.create(parents=True)

                data = DatabaseFactory.fromYear(dataset).parse()

                with raw_dir:
                    for raw_format in args.raw:
                        data.export(raw_format, 'auto')

                with minified_dir:
                    for minifiable_format in args.min:
                        data.export(minifiable_format, 'auto', minify=True)
        except KeyboardInterrupt:
            logger.info('> Building was canceled.')
