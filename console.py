#!/usr/bin/python3
import cmd
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command processor for the HBNB console."""

    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'Review': Review,
        # other classes...
    }

    def do_create(self, args):
        """Creates a new instance of a class."""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Shows the string representation of an instance."""
        # code to show...

    def do_destroy(self, args):
        """Destroys an instance based on the class name and id."""
        # code to destroy...

    def do_all(self, args):
        """Shows all instances of a class or all instances if no class is specified."""
        # code to display all...

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        # code to update...

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()










