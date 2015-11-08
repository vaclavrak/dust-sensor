# -*- coding: UTF-8 -*-

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dust-sensor',
    version='0.1',
    packages=['dust_sensor'],
    include_package_data=True,
    license='BSD License',  # example license
    description='work with arduino dust sensor',
    long_description=README,
    url='https://webeye.services/',
    author='Václav Rak',
    author_email='rak@webeye.services',
    classifiers=[
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)