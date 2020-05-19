#!/usr/bin/python3
""" class Square """


class Square:
    """empty class Square that defines a square

    Attributes:
        size (str): Description of size square.

    """

    def __init__(self, size=0):
        """empty class Square that defines a square

        Attributes:
            self (:obj:`list`): Description of `param3`
            size (str): Description of size square.

        """
        if (type(size) != int):
            raise ValueError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this area function

        return:
            area (int): This area of square
        """
        return (self.__size ** 2)
