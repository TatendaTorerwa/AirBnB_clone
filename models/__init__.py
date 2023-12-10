#!/usr/bin/python3
"""__init__.py Module that renders the directory a package"""

from models.engine import file_storage

storage = FileStorage()
storage.reload()
