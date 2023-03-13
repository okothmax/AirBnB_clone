#!/usr/bin/env python3

'''
Foundation(parent) class for the whole project
'''

import datetime
from uuid import uuid4
import models

class BaseModel:
    """
    Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    def __init__(self, *args, **kwargs):
        '''
        Public instance artributes initialization after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attribute values
        '''
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        A string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictory representation of the object
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
