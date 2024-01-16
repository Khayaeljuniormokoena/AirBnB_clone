#!/usr/bin/python3
"""
Test module for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """
    def test_attributes(self):
        """
        Test creation and attributes of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), str_rep)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
