#!/usr/bin/python3
"""
Test suits for amenities
"""
import os
from models.amenity import Amenity
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Tests for amenities
    """

    obj = Amenity()

    def setUp(self):
        """set initial"""
        name = ""

    def test_normal_cases_amenity(self):
        """normal cases"""
        my_object = Amenity()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Amenity")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_type(self):
        """test type of object"""
        obj = Amenity()
        self.assertEqual(type(self.obj.name), str)
if __name__ == '__main__':
    unittest.main()
