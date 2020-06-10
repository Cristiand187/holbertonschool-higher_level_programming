#!/usr/bin/python3
"""module class Base"""
import json
import csv


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def greater_validator(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            ValueError: [description]
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def greater_iqual_validator(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            ValueError: [description]
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        filename = cls.__name__+".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(
                    [cls.to_dictionary(elem) for elem in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or len(json_string) <= 0:
            return json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                json_obj = cls.from_json_string(f.read())
        except Exception:
            return []
        return [cls.create(**elem) for elem in json_obj]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        filename = cls.__name__+".csv"
        with open(filename, 'w', newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for elem in list_objs:
                writer.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        filename = cls.__name__+".csv"
        with open(filename, newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(f, fieldnames=fieldnames)
            list_dicts = [dict([key, int(value)] for key, value in d.items())
                          for d in list_dicts]
        return [cls.create(**elem) for elem in list_dicts]
