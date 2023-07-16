#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
import uuid
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represents store engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj instance in the __objects dictionary with the key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes the __objects dictionary to the JSON file"""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to the __objects dictionary"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
