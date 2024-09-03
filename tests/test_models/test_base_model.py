import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instantiation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertTrue(model.updated_at > model.created_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
