#!/usr/bin/python3
"""Tests for tha base"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class test_BaseClass(unittest.TestCase):
    """
        base test class
    """

    def test_standard(self):
        """[summary]
        """
        b1 = Base(12)
        b2 = Base(-12)
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, -12)
        self.assertEqual(type(b3.id), int)
        self.assertEqual(type(b4.id), int)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "{} Errors".format(result.total_errors))
