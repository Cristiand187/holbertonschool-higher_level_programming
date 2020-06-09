#!/usr/bin/python3
"""module class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle

    Args:
        Base ([class]): class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        Base.integer_validator(self, "width", width)
        Base.greater_validator(self, "width", width)
        Base.integer_validator(self, "height", height)
        Base.greater_validator(self, "height", height)
        Base.integer_validator(self, "x", x)
        Base.greater_iqual_validator(self, "x", x)
        Base.integer_validator(self, "y", y)
        Base.greater_iqual_validator(self, "y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter
        Returns:
            The size of the square
        """
        return self.__width

    @width.setter
    def width(self, value):
        Base.integer_validator(self, "width", value)
        Base.greater_validator(self, "width", value)

        self.__width = value

    @property
    def height(self):
        """getter
        Returns:
            The size of the square
        """
        return self.__height

    @height.setter
    def height(self, value):
        Base.integer_validator(self, "height", value)
        Base.greater_validator(self, "height", value)

        self.__height = value

    @property
    def x(self):
        """getter
        Returns:
            The size of the square
        """
        return self.__x

    @x.setter
    def x(self, value):
        Base.integer_validator(self, "x", value)
        Base.greater_iqual_validator(self, "x", value)

        self.__x = value

    @property
    def y(self):

        return self.__y

    @y.setter
    def y(self, value):
        Base.integer_validator(self, "y", value)
        Base.greater_iqual_validator(self, "y", value)

        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        print('\n' * self.__y, end="")
        for i in range(0, self.__height):
            print(' ' * self.__x, end="")
            for j in range(0, self.__width):
                print('#', end="")
            print()

    def __str__(self):
        str_self = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                    self.id, self.__x,
                                                    self.__y, self.__width,
                                                    self.__height)
        return str_self

    def update(self, *args, **kwargs):
        n_arg = len(args)
        list_attr = ["id", "width", "height", "x", "y"]
        if args is None or n_arg == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for x, arg in enumerate(args):
            setattr(self, list_attr[x], arg)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
