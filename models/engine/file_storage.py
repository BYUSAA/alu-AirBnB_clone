#!/usr/bin/env python
"""A module that that serializes instances to a JSON file and deserializes
JSON file to instances"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

from models.review import Review

# In the class FileStorage

class FileStorage:
    """Serializes instances to a JSON file and deserializes instances from a JSON file"""
    __file_path = 'file.json'
    __objects = {}

    # The dictionary of all classes
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'Review': Review,
        # other classes...
    }

    # private class attributes
    # __file_path is the path to the JSON file to store all objects.
    __file_path = 'storage.json'

    # __objects is a dictionary that stores all objects by <class name>.id
    # ex: to store a BaseModel object with id=12121212, the key will be
    # BaseModel.12121212 and the value will be the object.
    # the object (value of key) is stored like this:
    # <models.base_model.BaseModel object at 0x7f3329dac310>
    # obects = {BaseModel.12121212: }
    __objects = {}

        def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def all(self, cls=None):
        """Returns a list of all objects if cls is None. If cls is provided, return all objects of that type.
        """
        if cls is not None:

            obj = {}
            print(FileStorage.__objects.items())
            for key, val in FileStorage.__objects.items():
                if cls.__name__ in key:
                    obj[key] = val
            return obj
        else:
            return self.__objects

    # sets in __objects the obj with key <obj class name>.id

    def new(self, obj):
        """Adds new object to __objects dictionary"""
        """
        obj: the object with key <obj class name>.id
        """
        if obj:
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        # json_data = json.dump(obj)
        self.__objects[key] = obj

    # serializes __objects to the JSON file (path: __file_path)

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        # code to serialize...
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(objs, f)

    def reload(self):
        "Deserializes the JSON file to __objects"""
        # code to deserialize...
        """Deserializes the JSON file to __objects (only if the JSON file"""
        """(path: __file_path) exists ; otherwise, do nothing."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                json_obj = json.load(json_file)
                 for key, obj in objs.items():
                    cls_name = obj["__class__"]
                      if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**obj)
                    elif cls_name == "User":
                        self.__objects[key] = User(**obj)
                    elif cls_name == "Place":
                        self.__objects[key] = Place(**obj)
                    elif cls_name == "City":
                        self.__objects[key] = City(**obj)
                    elif cls_name == "Amenity":
                        self.__objects[key] = Amenity(**obj)
                    elif cls_name == "State":
                        self.__objects[key] = State(**obj)
                    elif cls_name == "Review":
                        self.__objects[key] = Review(**obj)
        except FileNotFoundError:
            pass
                    # By providing the dict value stored in json_obj[key] as
                    # kwargs, genrate an object with the same attributes
                    self.__objects[key] = eval(
                        json_obj[key]['__class__'])(**json_obj[key])

    def delete(self, obj=None):
        """Delete an object from the __objects"""
        if obj is not None:
            for key, val in list(FileStorage.__objects.items()):
                if obj == val:
                    del FileStorage.__objects[key]
                    print("Deleted: {}".format(key))
                    self.save()
                    
    def close(self):
        self.reload()







