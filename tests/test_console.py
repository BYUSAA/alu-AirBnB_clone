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

    def test_create(self):
        """Test create command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(f.getvalue().strip(), r'\w+-\w+-\w+-\w+-\w+')

    def test_show(self):
        """Test show command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123456")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_destroy(self):
        """Test destroy command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123456")
            self.assertEqual("", f.getvalue().strip())

    def test_all(self):
        """Test all command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual("", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual("", f.getvalue().strip())

    def test_update(self):
        """Test update command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 123456")
            self.assertEqual("** attribute name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 123456 name")
            self.assertEqual("** value missing **", f.getvalue().strip())

    def test_count(self):
        """Test count command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual("0", f.getvalue().strip())

    def test_help(self):
        """Test help command input."""
        with patch('sys.stdout', new
