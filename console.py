#!/usr/bin/python3
"""Command interpreter for the HBNB project."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True
        
    def emptyline(self):
        """Do nothing on empty line."""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()