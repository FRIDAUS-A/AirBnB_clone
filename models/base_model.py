#!/usr/bin/python3
"""DEFINES THE BASE CLASS FOR ALL ALL THE
OTHER CLASSES
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """THE BaseModel CLASS"""
    def __init__(self, *args, **kwargs):
        """INSTANCE CONSTRUCTOR
            ARGS:
                args: contains a tuple of l
                id (string): user id
                craeted_at: the time the user craete the account
                updated_at: the time the user updated the account
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        result = value
                        date, time = result.split('T')
                        year, month, day = date.split('-')
                        hour, minute, second = time.split(':')
                        main_sec, microsec = second.split('.')
                        self.__dict__[key] = datetime(
                                int(year), int(month), int(day),
                                int(hour), int(minute), int(main_sec),
                                int(microsec)
                                )
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        """string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        tmp_created = self.created_at
        tmp_updated = self.updated_at
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        instance = self.__dict__
        dic = {}
        for key, value in instance.items():
            dic[key] = value
        dic["__class__"] = self.__class__.__name__
        self.created_at = tmp_created
        self.updated_at = tmp_updated
        return dic
