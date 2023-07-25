# models/engine/file_storage.py

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                serialized_objs = json.load(file)
                for key, value in serialized_objs.items():
                    class_name, obj_id = key.split(".")
                    obj_cls = eval(class_name)
                    obj = obj_cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
