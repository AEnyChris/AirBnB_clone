#!/usr/bin/python3
"""This module contains the FileStorage class
class: FileStorage
        see FileStorage.__doc__ for details
"""
import json
import os
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel":BaseModel, "User":User}

class FileStorage:
    """FileStorage class for the
    serialization and deserialization of JSON strings
    """

    __file_path = 'file.json'  # string - path to json file
    __objects = {}  # dictionary - to hold objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets an object in __objects in form <obj class name>.id"""
        if obj is not None:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes obj into json file"""
        objs_to_dict = {}
        for key, obj in self.__objects.items():
            objs_to_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(objs_to_dict, fp)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fp:
                reloaded_objs_dict = json.load(fp)
            for key, dic in reloaded_objs_dict.items():
                self.__objects[key] = BaseModel(**dic)
