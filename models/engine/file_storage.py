#!/usr/bin/python3
"""Module for File Storage"""
import json


class FileStorage:
    """Serializes instances to a JSON file and
       Deserializes a JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__) + "." + str(obj.id)]\
        = obj#json.dumps(obj.to_dict())

    def save(self):
        """Serializes __objects to JSON file __file_path"""
        new_dict = {}
        for key, value in FileStorage.__objects.keys():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                new = json.load(file)
                for key, value in new.items():
                    new[key] = BaseModel(**value)
                FileStorage.__objects = new
        except FileNotFoundError:
            pass
