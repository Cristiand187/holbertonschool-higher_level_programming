#!/usr/bin/python3
""" class Retangule """


class Rectangle:
    """ class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter
        Returns:
            The size of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, valor):

        if type(valor) != int:
            raise TypeError("width must be an integer")
        elif (valor < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = valor

    @property
    def height(self):
        """getter
        Returns:
            The size of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, valor):

        if type(valor) != int:
            raise TypeError("height must be an integer")
        elif (valor < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = valor
