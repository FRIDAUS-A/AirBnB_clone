#!/usr/bin/env python3
"""Test cases for the BaseModel class"""
import unittest
from models.base_model import BaseModel

class test_instantiation_BaseModel(unittest.TestCase):
    """Testcase class for testing BaseModel instatiation"""
    def setUp(self):
        """called before running the test"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def tearDown(self):
        """called after running the test"""
        self.obj1 = None
        self.bj2 = None

    def test_BaseModel(self):
        """test if the object is an instance of the BaseModel class"""
        self.assertIsInstance(self.obj1, BaseModel)

    def test_id_string(self):
        """test if id is string"""
        self.assertIsInstance(self.obj1.id, str)

    def test_id_unique(self):
        """test if id unique"""
        self.assertNotEqual(self.obj1.id, self.obj2.id)
    
    def test_created_at_unique(self):
        """test if the created time is different"""
        self.assertNotEqual(self.obj1.created_at, self.obj2.created_at)

    def test_created_updated(self):
        """test if the created_at and updated_at is the same when first created"""
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)

    def test_updated_after_save(self):
        """test if the timse is updated after saving"""
        obj = BaseModel()
        time = obj.updated_at
        obj.save()
        time_after = obj.updated_at
        self.assertNotEqual(time, time_after)

    def test_created_at_isthesame(self):
        """test if the created time is constant"""
        obj = BaseModel()
        time = obj.created_at
        obj.save()
        time_after = obj.created_at
        self.assertEqual(time, time_after)

class test_string_representation(unittest.TestCase):
    """test the string representation of object"""
    maxDiff = None

    def setUp(self):
        """called before running the test"""
        self.obj = BaseModel()

    def tearDown(self):
        """called after running the test"""
        self.obj = None

    def test_string(self):
        """test string"""
        string = f"[{self.obj.__class__.__name__}] ({self.obj.id}) {self.obj.__dict__}"
        self.assertEqual(self.obj.__str__(), string)

class test_instance_method(unittest.TestCase):
    """test the instance methods"""

    def setUp(self):
        """called before running the test"""
        self.obj = BaseModel()

    def tearDown(self):
        """called after running the test"""
        self.obj = None

    def test_dict_class_(self):
        """test the to_dict method for class name"""
        self.assertEqual(self.obj.__class__.__name__, self.obj.to_dict()["__class__"])

if __name__ == '__main__':
    unittest.main()
