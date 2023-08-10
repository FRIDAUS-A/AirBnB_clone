#1/usr/bin/env python3
"""DEFINES THE BASE CLASS FOR ALL ALL THE
OTHER CLASSES
"""
import uuid
from datetime import datetime

class BaseModel:
    """THE BaseModel CLASS"""
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """INSTANCE CONSTRUCTOR
            ARGS:
                id (string): user id
                craeted_at: the time the user craete the account
                updated_at: the time the user updated the account
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing 
        all keys/values of __dict__ of the instance"""
        tmp_created = self.created_at
        tmp_updated = self.updated_at
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        instance = self.__dict__
        print(instance)
        dic = {}
        for key, value in instance.items():
            dic[key] = value
        dic["__class__"] = __class__.__name__
        self.created_at = tmp_created
        self.updated_at = tmp_updated
        return dic
