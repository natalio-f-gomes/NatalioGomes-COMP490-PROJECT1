"""
Author: Natalio Gomes
Class: COMP 490
Section: 003
File: conftest.py
Purpose: This file tells pytest to add the root directory to the Python path
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
