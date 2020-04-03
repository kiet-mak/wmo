# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in wmo/__init__.py
from wmo import __version__ as version

setup(
	name='wmo',
	version=version,
	description='Prototype for WMO',
	author='Ashfaq Khatri',
	author_email='kiet_mak@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
