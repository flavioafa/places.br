#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Main console script
'''
# Imports

# Package dependencies

from places.commands import Application

# Functions

def main():
    '''Main entry point.'''
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
