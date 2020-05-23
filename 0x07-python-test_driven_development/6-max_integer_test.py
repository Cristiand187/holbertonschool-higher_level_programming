#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_sum(self):
        """[summary]
        """

        self.assertEqual(max_integer([1, 2, 3]), 3)
