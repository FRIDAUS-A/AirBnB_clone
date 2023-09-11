#!/usr/bin/python3
"""INIT FILE"""

from models.engine.file_storage import FileStorage
from models import *
storage = FileStorage("./file.json")
storage.reload()
