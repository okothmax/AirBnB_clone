#!/usr/bin/python3
"""
Test suits for amenities
"""
import os
from models.review import Review
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Tests for amenities
    """

    obj = Review()

    def seUp(self):
        """set initial"""
        place_id = ""
        user_id = ""
        text = ""

    def test_normal_cases_review(self):
        """normal cases"""
        my_object = Review()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()
        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "Review")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(Review, BaseModel), True)
	
    def test_type(self):
        """test type of object"""
        self.assertEqual(type(self.obj.place_id), str)
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(type(self.obj.text), str)

if __name__ == "__main__":
    unittest.main()
