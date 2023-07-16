#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
import uuid

class FileStorage:
    """Represents store engine"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the __objects dictionary"""
        return FileStorage.__objects
        
    def new(self, obj):
        """Sets the obj instance in the __objects dictionary with the key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj
        
    def save(self):
        """Serializes the __objects dictionary to the JSON file"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)
            
    def reload(self):
        """Deserializes the JSON file to the __objects dictionary"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    FileStorage.__objects[k] = eval(
                        v['__class__'])(**v)
        except FileNotFoundError:
            pass
