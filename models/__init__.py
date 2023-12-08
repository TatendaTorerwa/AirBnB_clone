#!/usr/bin/python3
"""__init__.py Module that renders the directory a package"""

from engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
