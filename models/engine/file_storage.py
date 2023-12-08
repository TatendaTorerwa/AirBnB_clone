#!/usr/bin/python3
"""Module for File Storage"""
import json


class FileStorage:
    """Serializes instances to a JSON file and
       Deserializes a JSON file to instances
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """Returns the objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        __objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save(self):
        """Serializes __objects to JSON file __file_path"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file.read())
        except FileNotFoundError:
            pass
