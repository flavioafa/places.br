#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Property List file exporter module
'''
from __future__ import absolute_import

# Imports

# Built-in dependencies

import io
import re

# Package dependencies

from places.exporters import Exporter
from places.formats.plist import PlistFormat
from places.formats.plist.utils import PlistDumper, PlistWriter

# Classes


class PlistExporter(Exporter):
    '''
    Property List exporter class.
    '''

    # Exporter format
    _format = PlistFormat

    def export(self, **options):
        '''
        Exports the data into a Property List file-like stream.

        Arguments:
            options (dict): The exporting options

        Returns:
            io.BytesIO: A Property List file-like stream

        Raises:
            ExportError: When data fails to export
        '''
        data = self._data.normalize(strKeys=True, forceUnicode=True)
        plist_data = PlistDumper(data)

        if options.get('minify'):
            plist_data = re.sub('[\n\t]+', '', plist_data)

        return io.BytesIO(plist_data)
