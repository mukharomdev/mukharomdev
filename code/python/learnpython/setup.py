#! /usr/bin/env python

import os
import sys
import textwrap

from setuptools import setup

if __name__ == "__main__":
	
	setup(
	    name='learnpython',
	    version='0.0.1',
	    install_requires=[
	        'requests',
	        'importlib-metadata; python_version >= "3.8"',
	    ],
	)