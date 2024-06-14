#!/usr/bin/python3
"""This module implements a simple CLI"""

import cmd
import ast
import os, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

fs = FileStorage()
classes = {
        "BaseModel":BaseModel,
        "User":User,
        "Amenity":Amenity,
        "City":City,
        "Review":Review,
        "Place":Place,
        "State":State
        }

cls_missing = "** class name missing **"
cls_nonex = "** class doesn't exist **"
id_missing = "** instance id missing **"
inst_not_fnd = "** no instance found **"
attr_missing = "** attribute name missing **"
value_missing = "** value missing **"

                
class HBNBCommand(cmd.Cmd):
    """Simple command line interface for AirBnB clone project"""
    prompt = '(hbnb)'

    ## ERROR MANAGEMENT ###

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
                fs.reload()
                all_objs = fs.all()
                if f"{args[0]}.{args[1]}" not in all_objs.keys():
                    self.call_err_msg(inst_not_fnd)
                    return 0
                return 1, all_objs, args
            else:
                self.call_err_msg(id_missing)
                return 0


    def attr_check(self, line):
        flag = self.id_check(line)
        if flag:
            args = flag[2]
            all_objs = flag[1]
            if len(args) == 2:
                self.call_err_msg(attr_missing)
                return 0
            elif len(args) == 3:
                self.call_err_msg(value_missing)
                return 0
            else:
                return 1



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
            args = line.split()
            all_objs = fs.all()
            print(all_objs[f"{args[0]}.{args[1]}"])


    def do_destroy(self, line):
        """deletes an instance from record"""   
        if self.id_check(line):
            args = line.split()
            fs._FileStorage__objects.pop(f"{args[0]}.{args[1]}")
            fs.save()


    def do_all(self, line):
        """prints the string repr of all instances"""
        all_objs = fs.all()
        if not line:
            print([str(obj) for obj in all_objs.values()])
        else:
            if self.class_check(line):
                args = line.split()
                obj_list = [str(all_objs[key]) for key in all_objs.keys() if key.startswith(args[0])]
                print(obj_list)

    def count(self, line):
        all_objs = fs.all()
        if self.class_check(line):
            args = line.split()
            obj_list = [str(all_objs[key]) for key in all_objs.keys() if key.startswith(args[0])]
            print(len(obj_list))


    def do_update(self, line):
        """updates or adds attr to instance"""
        args = line.split()
        if self.attr_check(line):
            args = line.split()
            key = f"{args[0]}.{args[1]}"
            setattr(fs._FileStorage__objects[key], args[2], args[3])
            fs.save()

    def update2(self, *args, **kwargs):
        """Processes dictionary attribute input"""
        line = f"{args[0]} {args[1]}"
        if self.id_check(line):
            key = f"{args[0]}.{args[1]}"
            for attr, value in kwargs.items():
                setattr(fs._FileStorage__objects[key], attr, value)
            fs.save()
        

 
    def onecmd(self, line):
        """Define command formats"""
        commands = {
        "all": self.do_all,
        "create": self.do_create,
        "show": self.do_show,
        "destroy": self.do_destroy,
        "update":self.do_update,
        # "update2":self.do_update2
        "count": self.count
        }
        if "." in line:
            try:
                args = line.strip().split(".")
                class_name = args[0]
                command_line = args[1].split("(")
                command = command_line[0]
                parameter = command_line[1].strip(")")

                if "{" in parameter and command == 'update':
                    parameter = parameter.split(",", 1)
                    idx = parameter[0].replace('"', '')
                    if len(parameter) > 1:
                        attr_dict = ast.literal_eval(parameter[1].strip())
                        self.update2(class_name, idx, **attr_dict)
                        return
                    else:
                        self.call_err_msg(attr_missing)
                else:
                    parameter = parameter.replace("," , "").replace('"', '')
                    new_line = f"{class_name} {parameter}"
            
                if command not in commands.keys():
                    cmd.Cmd.default(self, command)
                else:
                    commands[command](new_line.strip())
            except Exception as e:
                cmd.Cmd.default(self, line)

                   
        else:
            cmd.Cmd.onecmd(self, line)


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
