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
    def test_return_max_integer_in_list_of_integers(self):
        """
        Test that function returns the max integer
        """
        max_num = max_integer([1, 5, 2, 3])
        self.assertEqual(max_num, 5)

    def test_return_max_integer_in_list_with_floats(self):
        """
        Test that function returns max integer with floats in the list
        """
        max_num = max_integer([1, 4, 5.5234, 0])
        self.assertEqual(max_num, 5.5234)
        max_num = max_integer([1, 4, 5.1234, 0])
        self.assertEqual(max_num, 5.1234)
        max_num = max_integer([1, 4, 5.1234, 5])
        self.assertEqual(max_num, 5.1234)

    def test_for_list_with_one_element(self):
        """
        Test that function returns the number of a list of length 1
        """
        max_num = max_integer([9])
        self.assertEqual(max_num, 9)
        max_num = max_integer([-9])
        self.assertEqual(max_num, -9)
        with self.assertRaises(TypeError):
            max_integer(5)
        with self.assertRaises(KeyError):
            max_integer({'a': 5})

    def test_negative_numbers_are_numbers_too(self):
        """
        Tests that function return max integer with negative numbers
        """
        max_num = max_integer([1, -2])
        self.assertEqual(max_num, 1)
        max_num = max_integer([-1, -2])
        self.assertEqual(max_num, -1)
        max_num = max_integer([-30, -0.45])
        self.assertEqual(max_num, -0.45)

    def test_list_with_non_number_types_raise_exception(self):
        """
        Tests that the function raises a TypeError if elements are not numbers
        """
        with self.assertRaises(TypeError):
            max_integer([1, 'hello', 2])
        with self.assertRaises(TypeError):
            max_integer([[1], 2])
        with self.assertRaises(TypeError):
            max_integer([1, {1: 400, 2: 450}, 23])

    def test_no_parameter_returns_none(self):
        """
        Test that None is returned if no argument is given
        """
        max_num = max_integer()
        self.assertEqual(max_num, None)

    def test_empty_list_returns_none(self):
        """
        Test that function returns None if list is empty
        """
        max_num = max_integer([])
        self.assertEqual(max_num, None)

    def test_all_elements_of_equal_value(self):
        """
        Test that max integer is returns for list of all equal elements
        """
        max_num = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(max_num, 5)


if __name__ == '__main__':
    unittest.main()
