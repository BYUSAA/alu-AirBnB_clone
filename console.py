#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application"""
    
    prompt = "(hbnb) "  # Custom prompt
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help <command>'"""
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
