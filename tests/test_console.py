import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Unittests for testing the console."""

    def test_empty_line(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_quit(self):
        """Test quit command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue().strip())

    def test_EOF(self):
        """Test EOF (Ctrl+D) input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("", f.getvalue().strip())

    def test_help(self):
        """Test help command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsNotNone(f.getvalue().strip())

    def test_create_BaseModel(self):
        """Test create BaseModel command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_User(self):
        """Test create User command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_State(self):
        """Test create State command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_City(self):
        """Test create City command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_Amenity(self):
        """Test create Amenity command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_Place(self):
        """Test create Place command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_create_Review(self):
        """Test create Review command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_show_BaseModel(self):
        """Test show BaseModel command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123456")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_User(self):
        """Test show User command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 123456")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_State(self):
        """Test show State command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State 123456")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_City(self):
        """Test show City command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City 123456")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_show_Amenity(self):
        """Test show Amenity command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity 
