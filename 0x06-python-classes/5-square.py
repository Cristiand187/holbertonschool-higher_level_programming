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

    @property
    def size(self):
        """getter

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, val):
        """setter
        Args:
            val (int): The size of the square
        Returns:
            None
        """
        if (type(val) != int):
            raise ValueError("size must be an integer")
        elif (val < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """this area function

        return:
            area (int): This area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """this my_print function

        return:
            None
        """
        n = 1 if self.__size == 0 else self.__size

        for i in range(n):
            for j in range(n):
                print(' ' if self.__size == 0 else '#', end='')
            print()
