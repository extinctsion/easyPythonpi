#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest

from easyPythonpi.methods.basics import *

class TestBasicMath(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_with_zero(self):
        self.assertEqual(add(0.5, 0.5), 1.0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(sub(5, 2), 3)

    def test_subtract_with_zero(self):
        self.assertEqual(sub(0, 0), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(sub(-1, -1), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multi(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multi(0, 5), 0)

    def test_multiply_by_negative_numbers(self):
        self.assertEqual(multi(-2, 6), -12)

    def test_divide_by_smaller_number(self):
        self.assertEqual(div(6, 2), 3.0)

    def test_divide_zero_by_number(self):
        self.assertEqual(div(0, 5), 0.0)

    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_mod_positive_numbers(self):
        self.assertEqual(mod(7, 3), 1)
        self.assertEqual(mod(10, 2), 0)

    def test_mod_zero(self):
        self.assertEqual(mod(0, 5), 0)

    def test_mod_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            mod(8, 0)


if __name__ == '__main__':
    unittest.main()
