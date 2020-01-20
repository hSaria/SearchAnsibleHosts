#!/usr/bin/env python3
"""SearchAnsibleHosts setup"""

from setuptools import setup

REQUIRES = ['ansible', 'psutil']
REQUIRES_PYTHON = '>=3.5.0'

with open('.github/README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='search-ansible-hosts',
    author='hSaria',
    author_email='ping@heysaria.com',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3', 'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    description='Ansible inventory searching for rapid use',
    license='MIT',
    install_requires=REQUIRES,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    python_requires=REQUIRES_PYTHON,
    scripts=['search-ansible-hosts'],
    setup_requires=REQUIRES,
    url='https://github.com/hSaria/SearchAnsibleHosts',
    version='0.0.2',
)
