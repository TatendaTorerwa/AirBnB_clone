#!/usr/bin/python3
"""Module for the console"""
import cmd


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
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
