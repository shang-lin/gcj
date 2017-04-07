from setuptools import setup, find_packages
import sys

setup(
    name = 'gcj',
    version = '1.0.0',
    packages = find_packages('src', exclude='tests'),
    package_dir = { '': 'src'}
)