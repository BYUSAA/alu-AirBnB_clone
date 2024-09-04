#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """Unittest for the BaseModel class."""

    def setUp(self):
        """Setup a new instance for testing."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created."""
        self.assertIsInstance(self.model, BaseModel)

    def test_unique_id(self):
        """Test if each instance has a unique ID."""
        new_model = BaseModel()
        self.assertNotEqual(self.model.id, new_model.id)

    def test_created_at(self):
        """Test if created_at is set during instantiation."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is set during instantiation and updated on save()."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary representation."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
