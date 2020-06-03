#!/usr/bin/python3
"""[summary]"""


class MyInt(int):
    """ Class that inherits from class int """

    def __eq__(self, other):
        """[summary]

        Arguments:
            other {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """[summary]

        Arguments:
            other {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        return int.__eq__(self, other)
