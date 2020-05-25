#!/usr/bin/python3
""" class Retangule """


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ class Rectangle that defines a rectangle

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.__width = width
        self.__height = height

    def __str__(self):

        R_str = ""
        if self.__width is 0 or self.__height is 0:
            return R_str

        for i in range(self.__height):
            for j in range(self.__width):
                R_str += "#"
            R_str += "\n" if (self.height - 1) != i else ""

        return R_str

    def __repr__(self):
        return "Rectangle(" + str(self.__height) + ", " + str(self.__width) + ")"

    @property
    def width(self):
        """getter
        Returns:
            The size of the square
        """
        return self.__width

    @width.setter
    def width(self, valor):

        if (type(valor) != int):
            raise TypeError("width must be an integer")
        elif (valor < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = valor

    @property
    def height(self):
        """getter
        Returns:
            The size of the square
        """
        return self.__height

    @height.setter
    def height(self, valor):

        if (type(valor) != int):
            raise ValueError("height must be an integer")
        elif (valor < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = valor

    def area(self):

        return self.__height * self.__width

    def perimeter(self):

        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)
