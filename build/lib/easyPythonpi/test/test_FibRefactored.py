#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest

from easyPythonpi.methods.basics import fibonacci
from easyPythonpi.easyPythonpi import InvalidNumberFibException


class TestFibRefactored(unittest.TestCase):
    def test_fibonacci_0(self):
        with self.assertRaises(InvalidNumberFibException):
            fibonacci(0)  

    def test_fibonacci_negative_number(self):
        with self.assertRaises(InvalidNumberFibException):
            fibonacci(-10)          

    def test_fibonacci_1(self):
        self.assertEqual( fibonacci(1), 0)    

    def test_fibonacci_2(self):
        self.assertEqual( fibonacci(2), 1)      

    def test_fibonacci_3(self):
        self.assertEqual( fibonacci(3), 1)   

    def test_fibonacci_4(self):
        self.assertEqual( fibonacci(4), 2)        

    def test_fibonacci_5(self):
        self.assertEqual( fibonacci(5), 3) 

    def test_fibonacci_6(self):
        self.assertEqual( fibonacci(6), 5) 

    def test_fibonacci_7(self):
        self.assertEqual( fibonacci(7), 8)  

    def test_fibonacci_8(self):
        self.assertEqual( fibonacci(8), 13)                           
            
    def test_fibonacci_9(self):
        self.assertEqual( fibonacci(9), 21)  

    def test_fibonacci_10(self):
        self.assertEqual( fibonacci(10), 34)    

if __name__ == '__main__':
    unittest.main()
