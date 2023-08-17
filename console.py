#!/usr/bin/python3
"""a program called console.py that contains 
the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import json
from models import storage

arr = ("User", "BaseModel")
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line == "User":
            line = User()
        elif line == "BaseModel":
            line = BaseModel()
        elif not line:
            print("** class name missing **")
        elif line not in arr:
            print("** class doesn't exist **")
        line.save()
        print(line.id)

    def do_show(self, args):
        """prints the string representation of an
        instance based on the class name and id
        """
        if args:
            arg = args.split()
        if not args:
            print("** class name missing **")
        elif arg[0] not in arr and len(arg) == 1:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            content = storage.all()
            tmp_model = None
            for key, value in content.items():
                if arg[1] == value.to_dict()["id"]:
                    if arg[0] == "User":
                        tmp_model = User(**(value.to_dict()))
                    elif arg[0] == "BaseModel":
                        tmp_model = BaseModel(**(value.to_dict()))
            if not tmp_model:
                print("** no instance found **")
            else:
                print(tmp_model)

    def do_destroy(self, args):
        """"
        Deletes an instance based on the class name and 
        id (save the change into the JSON file).
        """
        if args:
            arg = args.split()
        if not args:
            print("** class name missing **")
        elif arg[0] not in arr and len(arg) == 1:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            content = storage.all()
            signal = None
            for key, value in content.items():
                if arg[1] == value.to_dict()["id"]:
                    signal = "yes"
                    key_value = key
            if signal == "yes":
                content.pop(key_value)
            storage.save()

    def do_clear(self, line):
        """clear the screen
        Usage: clear
        """
        import os
        os.system("clear")

    def do_all(self, line):
        """ 
        Prints all string representation of all 
        instances based or not on the class name.
        """
        if line not in arr:
            print("** class doesn't exist **")
        else:
            all_list = []
            content = storage.all()
            for value in content.values():
                if line == "User":
                    all_list.append(User(**(value.to_dict())).__str__())
                if line == "BaseModel":
                    all_list.append(BaseModel(**(value.to_dict())).__str__())
            print(all_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name 
        and id by adding or updating attribute (
        save the change into the JSON file)
        """
        if args:
            arg = args.split()
        if not args:
            print("** class name missing **")
            return
        elif arg[0] not in arr and len(arg) == 1:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        content = storage.all()
        signal = None
        for value in content.values():
            if arg[1] == value.to_dict()["id"]:
                signal = "yes"
        if not signal:
            print("** no instance found **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        else:
            for key, value in content.items():
                if arg[1] == value.to_dict()["id"]:
                    kwargs = value.to_dict()
                    kwargs[arg[2]] = arg[3]
                    content[key] = User(**kwargs)
            storage.save()
if __name__ == "__main__":
    HBNBCommand().cmdloop()
