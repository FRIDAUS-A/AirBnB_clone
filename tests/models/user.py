#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
        """The constructor for the user class"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
