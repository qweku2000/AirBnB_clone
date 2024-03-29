#!/usr/bin/python3

import uuid
from datetime import datetime


format = "%Y-%m-%dT%H:%M:%s.%f"

"""BaseModel class for derivation of all other future classes"""
class BaseModel:
    """ Initialization of BaseModel"""
    def __init__(self,*args,**kwargs):
        if (kwargs):
            for key,value in kwargs.items():
                setatrr(self,key,value)
            if hasattr(self,"created_at") and type(self.created_at) is string:
                self.created_at = datetime.strptime(kwargs["created_at"],format)
            if hasattr(self,"updated_at") and type(self.updated_at) is string:
                self.updated_at = datetime.strptime(kwargs["updated_at"],format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        
    """String representation of BaseModel"""
    def __str__(self):
        print("[{:s}] ({:s}) {}",self.__class__.__name__,self.id,self.__dict__)

        
    """updates updated_at attibute with current time"""
    def save(self):
        self.updated_at = datetime.now()

        
    """returns dict that contains all keys and values of the instance"""
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.name
        if "created_at" in obj_dict:
            obj_dict["created_at"] = obj_dict["created_at"].strftime(time)
        if "updated_at" in obj_dict:
            obj_dict["updated_at"] = obj_dict["updated_at"].strftime(time)
        return obj_dict
        
    
