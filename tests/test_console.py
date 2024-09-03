import unittest
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNB command interpreter"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        self.assertTrue(self.console.onecmd("help"))

    def test_emptyline(self):
        """Test no command passed (empty line)"""
        self.assertFalse(self.console.onecmd(""))

    def test_create_BaseModel(self):
        """Test create command for BaseModel"""
        self.console.onecmd("create BaseModel")
        model_id = storage.all().keys()
        self.assertIn("BaseModel", model_id)

    def test_show_BaseModel(self):
        """Test show command for BaseModel"""
        new_model = BaseModel()
        storage.new(new_model)
        self.console.onecmd(f"show BaseModel {new_model.id}")
        output = self.console.stdout.getvalue()
        self.assertIn(new_model.id, output)

    def test_destroy_BaseModel(self):
        """Test destroy command for BaseModel"""
        new_model = BaseModel()
        storage.new(new_model)
        self.console.onecmd(f"destroy BaseModel {new_model.id}")
        self.assertNotIn(new_model.id, storage.all())

    def test_all_BaseModel(self):
        """Test all command for BaseModel"""
        self.console.onecmd("all BaseModel")
        output = self.console.stdout.getvalue()
        self.assertIn("BaseModel", output)

    def test_update_BaseModel(self):
        """Test update command for BaseModel"""
        new_model = BaseModel()
        storage.new(new_model)
        self.console.onecmd(f'update BaseModel {new_model.id} name "test_name"')
        self.assertEqual(new_model.name, "test_name")

    def test_model_methods(self):
        """Test .all(), .count(), .show(), .destroy(), .update() for all models"""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        for cls in classes:
            with self.subTest(cls=cls):
                model = cls()
                storage.new(model)

                # Test .all()
                self.console.onecmd(f'all {cls.__name__}')
                output = self.console.stdout.getvalue()
                self.assertIn(model.id, output)

                # Test .count()
                self.console.onecmd(f'count {cls.__name__}')
                output = self.console.stdout.getvalue()
                self.assertIn('1', output)

                # Test .show()
                self.console.onecmd(f'show {cls.__name__} {model.id}')
                output = self.console.stdout.getvalue()
                self.assertIn(model.id, output)

                # Test .destroy()
                self.console.onecmd(f'destroy {cls.__name__} {model.id}')
                self.assertNotIn(model.id, storage.all())

                # Test .update() with string attribute
                model = cls()
                storage.new(model)
                self.console.onecmd(f'update {cls.__name__} {model.id} name "new_name"')
                self.assertEqual(model.name, "new_name")

                # Test .update() with dictionary
                self.console.onecmd(f'update {cls.__name__} {model.id} {{"name": "dict_name"}}')
                self.assertEqual(model.name, "dict_name")

if __name__ == '__main__':
    unittest.main()
