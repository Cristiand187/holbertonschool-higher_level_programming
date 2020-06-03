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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
