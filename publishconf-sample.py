# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sample file to copy to ../website/publishconf.py

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import sys
from os import path

# Set the global shared PUBLISH flag to True. Since in our setup pelicanconf.py and publishconf.py
# are not in the same directory, they don't share globals. So we need a separate module so that
# this flag is set before pelicanconf is loaded.
sys.path.append(path.join('..', 'engine'))
from pelicanglobals import PUBLISH

PUBLISH = True

# Load configuration
from pelicanconf import *

# And add publication settings
SITEURL = 'http://example.com'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
