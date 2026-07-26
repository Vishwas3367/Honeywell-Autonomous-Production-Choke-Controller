"""
utils.py
Utility functions
"""

import os


def create_folder(folder):

    if not os.path.exists(folder):
        os.makedirs(folder)