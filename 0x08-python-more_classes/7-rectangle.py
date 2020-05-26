#!/usr/bin/python3
""" class Retangule """


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ class Rectangle that defines a rectangle

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):

        R_str = ""
        if self.__width is 0 or self.__height is 0:
            return R_str

        for i in range(self.__height):
            for j in range(self.__width):
                R_str += str(self.print_symbol)
            R_str += "\n" if (self.height - 1) != i else ""

        return R_str

    def __repr__(self):

        s = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return s

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            raise TypeError("height must be an integer")
        elif (valor < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = valor

    def area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__height * self.__width

    def perimeter(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)
