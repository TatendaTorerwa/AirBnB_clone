#!/usr/bin/python3
"""Module for the console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',\
            'Place', 'Review']

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
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        new = global()[line]
        new.save()
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance
           based on class name and id"""
        if not line:
            print("** class name missing **")
            return
        
        args = line.split()
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            print(storage.all()[args[0] + "." + args[1]])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and ID"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints a string representation off all
        objects based, or not on the class name"""
        args = line.split()
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            if args:
                instances = [str(obj) for obj in objects.values()
                             if type(obj).__name__ == args[0]]
            else:
                instances = [str(obj) for obj in objects.values()]
            print(instances)
	
    def do_update(self, line):
        """updates an instance based on class name and id"""
        args = line.split()

        if not args or args[0] not in HBNBCommand.classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
        	print("** attribute name missing **")
        elif len(args) < 4:
        	print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()

            if key not in objects:
                print("** no instance found **")
            else:
                attribute_name, value = args[2], args[3]
                obj = objects[key]
                try:
                    if not hasattr(obj, attribute_name):
                        print("** no attribute found **")
                        return

                    value = type(getattr(obj, attribute_name))(value)
                    setattr(obj, attribute_name, value)
                    obj.save()
                except ValueError:
                    print("** invalid value **")
                    return
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
