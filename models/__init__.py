#!/usr/bin/python3
"""__init__.py Module that renders the directory a package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
