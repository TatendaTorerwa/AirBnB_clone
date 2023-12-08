#!/usr/bin/python3
"""Module for the console"""
import cmd
from models.base_model import BaseModel
from models.engine import file_storage


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = "(hbnb) "

    def emptyline(self):
        """reprompts when user press Enter on an empty line"""
        pass

    def do_quit(self, line):
        """quit to exit the cmd loop"""
        return True

    def do_EOF(self, line):
        """Control D to successfully exit loop"""
        print()
        return True
    
    def do_create(self, line):
        """Creates new instance of BaseModel, saves it to JSON
           and prints its id"""
        if not line:
            print('** class name missing **')
        try:
            new_base_model = line()
        except NameError:
            print("** class doesn't exist **")
        new_base_model.save()
        print(new_base_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
           based on class name and id"""
        if not line:
            print("** class name missing **")
            return
        try:
            if not isinstance(line.split()[0](), object):
                raise NameError
        except NameError:
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
