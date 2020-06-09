#!/usr/bin/python3
"""Tests square"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_RectangleClass(unittest.TestCase):
    """base test class"""

    def test_standard(self):
        """[summary]
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "{} Errors".format(result.total_errors))
