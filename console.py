#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        obj_list = []
        if not args:
            for obj_key, obj in storage.all().items():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for obj_key, obj in storage.all().items():
                if obj_key.startswith(args[0] + "."):
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[obj_key]
                setattr(obj, args[2], args[3][1:-1] if '"' in args[3] else args[3])
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
