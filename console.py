#!/usr/bin/python3
"""This module implements a simple CLI"""

import cmd
import os, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

fs = FileStorage()

classes = {"BaseModel":BaseModel}

cls_missing = '"** class name missing **"'
cls_nonex = "** class doesn't exist **"
id_missing = "** instance id missing **"
inst_not_fnd = "** no instance found **"
attr_missing = "** attribute name missing **"

                
class HBNBCommand(cmd.Cmd):
    """Simple command line interface for AirBnB clone project"""
    prompt = '(hbnb)'

    def call_err_msg(self, msg):
        """prints error message"""
        self.nohelp = msg
        print(self.nohelp)

    def class_check(self, line):
        """checks and validates the class name in command line"""
        if not line:
            self.call_err_msg(cls_missing)
            return 0
        else:
            args = line.split()[:4]
            if len(args) >= 1:
                if args[0] not in classes.keys():
                    self.call_err_msg(cls_nonex)
                    return 0
                return 1, args

    def id_check(self, line):
        """checks and validates the id arg in command line"""
        flag = self.class_check(line)
        if flag:
            args = flag[1]
            if len(args) > 1:
                ids = []
                fs.reload()
                all_objs = fs.all()
                for key in all_objs.keys():
                    ids.append(key.split(".")[1])
                if args[1] not in ids:
                    self.call_err_msg(inst_not_fnd)
                    return 0
                return 1, all_objs, args
            else:
                self.call_err_msg(id_missing)
                return 0

    '''def attr_check(self, line):
        flag = self.id_check(line)
        if flag:
            args = flag[2]
            all_objs = flag[1]
            if len(args) > 2:
                try:
                    for key, obj in all_objs.items():
                        value = getattr(obj, args[2])
                        return 1, all_objs, args, value
                except:
                    self.call_err_msg(attr_missing)
                    return 0
            elif len(args) > 3:'''




    #### THE COMMANDS ###

    def do_create(self, line):
        """creates a new instance and saves it"""
        if self.class_check(line):
            new_inst = classes[line]()
            new_inst.save()
            print(new_inst.id)
            

    def do_show(self, line):
        """prints details of instance"""
        if self.id_check(line):
            id_check_value = self.id_check(line)
            args = id_check_value[2]
            all_objs = id_check_value[1]
            print(all_objs[f"{args[0]}.{args[1]}"])

    def do_destroy(self, line):
        """deletes an instance from record"""   
        if self.id_check(line):
            id_check_value = self.id_check(line)
            args = id_check_value[2]
            fs._FileStorage__objects.pop(f"{args[0]}.{args[1]}")
            fs.save()
            print(f"instance {args[1]} destroyed")
    
    def do_all(self, line):
        """prints the string repr of all instances"""
        all_objs = fs.all()
        if not line:
            print([str(obj) for obj in all_objs.values()])
        else:
            if self.class_check(line):
                flag = self.class_check(line)
                args = flag[1]
                obj_list = [str(all_objs[key]) for key in all_objs.keys() if key.startswith(args[0])]
                print(obj_list)

    def do_update(self, class_name, instance_id, attr, attr_val):
        """updates or adds attr to instance"""
        pass

    def do_quit(self, arg):
        """Quit command: Exits the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """ EOF: quits program"""
        return True

    ###### THE HELPS #######
    def help_create(self):
        print("create: Creates a new instance from class name\n"+\
        "Example usage: `create BaseModel`\n")

    def help_show(self):
        print("show displays the string representation of instance\n" +\
                "usage: show <class_name> <id>")

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

    do_q = do_quit

if __name__=='__main__':
    HBNBCommand().cmdloop()
