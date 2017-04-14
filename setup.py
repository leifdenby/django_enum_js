#!/usr/bin/env python

# Copyright 2014 Leif Denby

import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-enum-js',
    version='0.2',
    packages=['django_enum_js'],
    include_package_data=True,
    license='MIT',
    long_description=README,
    url='https://github.com/leifdenby/django_enum_js',
    author='Leif Denby',
    author_email='leif@denby.eu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
