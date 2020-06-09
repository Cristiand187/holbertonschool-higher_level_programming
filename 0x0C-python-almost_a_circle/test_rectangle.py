#!/usr/bin/python3
"""Tests for tha base"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class test_RectangleClass(unittest.TestCase):
    """
        base test class
    """

    def test_standard(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "{} Errors".format(result.total_errors))


if __name__ == '__main__':
    unittest.main()
