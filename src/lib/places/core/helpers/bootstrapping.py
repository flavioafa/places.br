#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2016 Paulo Freitas
# MIT License (see LICENSE file)
'''
Bootstrapping helper module

This module provides methods to bootstrap packages and modules.
'''
# Imports

# Built-in dependencies

import importlib
import pkgutil
import sys

# Classes


class ModuleLoader(object):
    '''
    Module loader class.
    '''

    @staticmethod
    def load(module):
        '''
        Loads a given module.

        Arguments:
            module (str): The module name to load

        Returns:
            module: The given module class
        '''
        if module in sys.modules:
            return sys.modules[module]

        return importlib.import_module(module)

    @classmethod
    def loadModules(cls, package, ignoreError=False):
        '''
        Loads a given package modules.

        Arguments:
            package: The package name or instance to load modules
            ignoreError (bool): Whether it should ignore import errors or not

        Returns:
            tuple: The loaded package module classes

        Raises:
            ImportError: When a package module can't be imported
            InvalidPackageError: When a given package is not valid
        '''
        if isinstance(package, str):
            package = cls.load(package)

        loaded_modules = ()

        try:
            namespace = package.__name__ + '.'

            for _, name, _ in pkgutil.walk_packages(package.__path__,
                                                    namespace):
                module = cls.load(name)
                loaded_modules += (module,)
        except ImportError:
            if not ignoreError:
                raise
        except AttributeError:
            raise InvalidPackageError('The given package is not valid')

        return loaded_modules

class InvalidPackageError(Exception):
    '''
    Exception class raised when a package is not valid.
    '''
    pass
