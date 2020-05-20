#!/usr/bin/python3
""" class Square """


class Square:
    """empty class Square that defines a square

    Attributes:
        size (str): Description of size square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """empty class Square that defines a square

        Attributes:
            self (:obj:`list`): Description of `param3`
            size (str): Description of size square.

        """
        self.size = size
        self.position = position

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
        if self.__size == 0:
            print()
            return

        for a in range(self.__position[1]):
            print()

        n = 1 if self.__size == 0 else self.__size

        for i in range(n):
            for k in range(self.__position[0]):
                print('' if self.__size == 0 else ' ', end='')
            for j in range(n):
                print('' if self.__size == 0 else '#', end='')
            print()

    @property
    def position(self):
        """getter

        Returns:
            The size of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter
        Args:
            value (int): The size of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
