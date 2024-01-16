#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            kwargs (dict): Dictionary representation of the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add the instance to storage

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        and calls the save method of storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
