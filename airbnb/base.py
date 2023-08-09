#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from time import sleep


class BaseModel:
    """
    base_model that defines all attribute
    """
    def __init__(self, *args, **kwargs):
        """init method for BaseModel Class"""

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime\
                                       .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    continue
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str method for BaseModel Class

            Return:
                string (str): string descriptor for BaseModel Class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the  updated_at attribute with the
        current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        dictFormat = {}

        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            # get the values which are of datetime object type
            if isinstance(val, datetime):
            #convert them to string objects in ISO format
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat 






