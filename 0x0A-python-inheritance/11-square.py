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


class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """[summary]

        Arguments:
            width {[type]} -- [description]
            height {[type]} -- [description]
        """
        super().integer_validator("width", width)
        self._Rectangle__width = width
        super().integer_validator("height", height)
        self._Rectangle__height = height

    def area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return "[{}] {}/{}".format(
                str(self.__class__.__name__), str(self._Rectangle__width), str(self._Rectangle__height))


class Square(Rectangle):

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
