#!/usr/bin/env python3
"""To store all objects"""

import json


class FileStorage():
    """serializes instances to a JSON file and
    deserializes JSON file to instances
        Args:
            file_path (string): defines the path to the json
            storage file
            objects (dict): contains the dictionary list
            of all the objects
        """
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        from models.user import User
        obj = User(**obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] =value.to_dict()
        try:
            with open(FileStorage.__file_path, "w") as file:
                file.write(json.dumps(new_dict))
        except FileNotFoundError:
            return


    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        from models.user import User
        try:
            with open(FileStorage.__file_path, "r") as file:
                content = file.read()
                content = json.loads(content)
                for key, value in content.items():
                    FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            return
