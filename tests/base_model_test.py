#!/usr/bin/env python3
"""Test cases for the BaseModel class"""

import unittest
from base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """Testcase class for the BaseModel class"""

    def test_idstring(self):
        """Test if id is a string"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_uniqueid(self):
        """Test if the id is unique"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        """check if the time created is different"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.created_at, obj2.created_at)

    def test_updated_at_initially(self):
        """check if the time the updated was first given is
        different for different obj cases
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_unique_created_updated(self):
        """check if the created time and updated time is different"""
        obj = BaseModel()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_updated_at_saved(self):
        """check if it the time updated is differnt when saved"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        self.assertNotEqual(obj1.updated_at, obj2.created_at)

    def test_to_dict(self):
        """Test the return value of to_dict() method"""
        my_model = BaseModel()
        id = my_model.id
        created_at = str(my_model.created_at.isoformat())
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        updated_at = str(my_model.updated_at.isoformat())
        my_model_json = my_model.to_dict()
        expected_result_todict = {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': updated_at, 'id': id, 'created_at': created_at}
        self.assertEqual(my_model_json, expected_result_todict)

if __name__ == "__main__":
    unittest.main()
