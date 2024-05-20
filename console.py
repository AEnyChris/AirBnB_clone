#!/usr/bin/python3


import cmd
import os, sys

class HBNBCommand(cmd.Cmd):
    """Simple command line interface for AirBnB clone project"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command: Exits the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """ EOF: quits program"""
        return True
    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

    def do_clear(self, arg):
        os.system('clear')
    
    def help_clear(self):
        print("clear the terminal\n")

if __name__=='__main__':
    HBNBCommand().cmdloop()
