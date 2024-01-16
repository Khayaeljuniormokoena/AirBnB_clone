# tests/test_models/test_base_model.py
#!/usr/bin/python3
"""Test cases for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Define test cases for BaseModel class."""

    def test_base_model_instance(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_base_model_str(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        self.assertIn("[BaseModel] ({})".format(my_model.id), str(my_model))

    def test_base_model_save(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
