#!/usr/bin/python3
"""
This module defines the base model from which other classes are created.

class: BaseModel()
    See BaseModel.__doc__ for details on the class
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Superclass Basemodel for the creation of other classes"""

    def __init__(self):
        """constructor method to initialize an instance"""
        self.id = str(uuid4())  # id: a unique id for each instance created
        self.created_at = datetime.now()  # the time instance was created

        # the current time instance was created. Updated when object is changed
        self.updated_at = self.created_at

    def __str__(self):
        """changes the display of the instance"""
        return f'[{self.__class__.__name}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the 'updated_at' attribute of
        the instance to the current time of change
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """converts the instance into a dictionary object"""
        instance_dict = {}
        instance_dict[dir(self)[0]] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                instance_dict[key] = value.isoformat()
            else:
                instance_dict[key] = value

        return instance_dict
