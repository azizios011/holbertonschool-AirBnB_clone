#!/usr/bin/python3
""" the file_storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name_obj, obj.id)] = obj

    def save(self):
        dict_ = FileStorage.__objects
        obj_dict = {key: dict_[key].to_dict() for key in dict_.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):

        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for val in obj_dict.values():
                    name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(name)(**val))
        except FileNotFoundError:
            return
