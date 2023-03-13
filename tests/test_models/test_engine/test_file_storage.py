"""Unittests for base model class"""


import unittest
from models.engine import file_storage

class TestsFileStorage(unittest.TestCase):

    def test_normal_cases_base_model(self):
        """normal cases"""
        my_object = file_storage.FileStorage()
        my_dict = my_object.all()
        self.assertIs(type(my_dict), dict)

if __name__ == '__main__':
    unittest.main()
