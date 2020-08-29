"""
minesweeper.py (minesweeperPy)
A simple minesweeper grid generator for Python 3

Version: 2.0
"""

__title__ = "minesweeperPy"
__author__ = "Steven Shrewsbury"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2019 Steven Shrewsbury"
__version__ = "2.0"
__URL__ = "https://github.com/stshrewsburyDev/minesweeperPy"

from .generator import Generator
from .preset import Presets, generate_preset, generate_preset_raw
from .error import *
