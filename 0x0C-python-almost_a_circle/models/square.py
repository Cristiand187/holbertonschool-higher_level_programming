#!/usr/bin/python3
"""module class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square

    Args:
        Rectangle ([Class]): [class Rectangle]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        str_self = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                 self.id, self.x,
                                                 self.y, self.width)
        return str_self

    def update(self, *args, **kwargs):
        """[summary]
        """
        n_arg = len(args)

        list_attr = ["id", "size", "x", "y"]
        if args is None or n_arg == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for x, arg in enumerate(args):
            setattr(self, list_attr[x], arg)

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, val):
        """[summary]

        Args:
            val ([type]): [description]
        """
        self.width = val
        self.height = val
