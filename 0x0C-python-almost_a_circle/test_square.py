#!/usr/bin/python3
"""Tests square"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class test_RectangleClass(unittest.TestCase):
    """test class square"""

    def test_standard(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/Square.py'])
        self.assertEqual(result.total_errors, 0,
                         "{} Errors".format(result.total_errors))


if __name__ == '__main__':
    unittest.main()
