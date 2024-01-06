#!/usr/bin/python3
"""This module instantiates an instance of the Storage will be used"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

StorageType = getenv('HBNB_TYPE_STORAGE')
if StorageType == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
