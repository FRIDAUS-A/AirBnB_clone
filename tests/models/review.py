#1/usr/bin/python3
"""Inherit from the BaseModel class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review"""
    place_id = ""
    user_id = ""
    text = ""
