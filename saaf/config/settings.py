"""
SAAF Configuration Settings

Central place for application configuration.
"""

import os


# Base project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# Database configuration
DATABASE_DIR = os.path.join(
    BASE_DIR,
    "data"
)


DATABASE_PATH = os.path.join(
    DATABASE_DIR,
    "saaf_memory.db"
)