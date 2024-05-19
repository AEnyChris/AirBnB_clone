#!/usr/bin/python3
"""initialize appliation with a unique FileStorage instance"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()



