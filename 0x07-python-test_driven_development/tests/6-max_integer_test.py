#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_max(self):
        """[summary]
        """

        self.assertEqual(max_integer([1, 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()
