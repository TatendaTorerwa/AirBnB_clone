#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
<<<<<<< HEAD
=======
import models
>>>>>>> a484b7494f37c12cec7cd1035c0e9c95c99ac6cc


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """Initialize a new BaseModel.
=======
        if kwargs:
            for name, value in kwargs.items():
                match name:
                    case "__class__":
                        continue
                    case "updated_at" | "created_at":
                        value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
>>>>>>> a484b7494f37c12cec7cd1035c0e9c95c99ac6cc

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
<<<<<<< HEAD
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
        """Updates the the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary, __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['updated_at'] = str(self.updated_at.isoformat())
        instance_dict['created_at'] = str(self.created_at.isoformat())
        return instance_dict
>>>>>>> a484b7494f37c12cec7cd1035c0e9c95c99ac6cc
