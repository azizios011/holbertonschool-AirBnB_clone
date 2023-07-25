#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "Place",
                     "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """ exit the program """
        return True

    def do_EOF(self, arg):
        """ exit with ctrl + D """
        return True

    def emptyline(self):
        """ an empty line is entered (do nothing) """
        pass

    def do_create(self, arg):
        """create a new instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representantion of a instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """Deletes and instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """print all string representations of instances"""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            filtered_instances = [
                    str(instance)
                    for instance in instances.values()
                    if instance.__class__.__name__ == class_name
            ]
            print(filtered_instances)

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
