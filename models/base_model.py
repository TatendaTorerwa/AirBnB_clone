#!/usr/bin/python3
"""The Base Model Module"""
import uuid
import datetime

class BaseModel:
    """The base model class that defines all the common
       attributes and methods for all the other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates the the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary, __dict__ of the instance"""
        instance_dict = self.__dict__
        instance_dict['__class__'] = str(self.__class__.__name__)
