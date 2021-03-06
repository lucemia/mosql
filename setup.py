#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup
from mosql import __version__

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name = 'mosql',
    description = "Build SQL with native Python data structure smoothly.",
    long_description = open('README.rst').read(),
    version = __version__,
    author = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    url = 'http://mosql.mosky.tw/',
    packages = ['mosql'],
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    **extra
)

