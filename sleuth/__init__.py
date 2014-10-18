"""
Sleuth: A debugging and diagnostic tool for Python.
------
"""

import sys
if sys.version_info[:2] < (3, 0):
    raise ImportError("Sleuth requires Python 3.")
del sys

__version__ = '0.1.0'

from .__main__ import main
from .sleuth import *
from .error import *
