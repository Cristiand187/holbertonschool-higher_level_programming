#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry():
    """
    BaseGeometry
    """
    pass

    def area(self):
        """[summary]

        Raises:
            ValueError: [description]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[summary]

        Arguments:
            name {[type]} -- [description]
            value {[type]} -- [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
