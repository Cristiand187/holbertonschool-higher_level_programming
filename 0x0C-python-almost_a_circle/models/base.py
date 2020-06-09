#!/usr/bin/python3
"""module class Base"""
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def greater_validator(self, name, value):

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def greater_iqual_validator(self, name, value):

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__+".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(
                    [cls.to_dictionary(elem) for elem in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) <= 0:
            return json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):

        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                json_obj = cls.from_json_string(f.read())
        except Exception:
            return []
        return [cls.create(**x) for x in json_obj]
