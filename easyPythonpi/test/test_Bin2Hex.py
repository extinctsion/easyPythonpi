#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
import easyPythonpi.easyPythonpi as pi

from easyPythonpi.methods.basics import *


class TestBin2Hex(unittest.TestCase):
    def test_single_binary_zero(self):
        self.assertEqual( bin2hex('0'), '0')

    def test_single_binary_one(self):
        self.assertEqual( bin2hex('1'), '1')     

    def test_binary_two_zeros(self):
        self.assertEqual( bin2hex('00'), '0')   

    def test_binary_three_zeros(self):
        self.assertEqual( bin2hex('000'), '0')   

    def test_binary_four_zeros(self):
        self.assertEqual( bin2hex('0000'), '0')   

    def test_binary_1111_to_hex(self):
        self.assertEqual( bin2hex('1111'), 'F')   

    def test_binary_1110_to_hex(self):
        self.assertEqual( bin2hex('1110'), 'E')   

    def test_binary_1101_to_hex(self):
        self.assertEqual( bin2hex('1101'), 'D')    

    def test_binary_1100_to_hex(self):
        self.assertEqual( bin2hex('1100'), 'C')

    def test_binary_1011_to_hex(self):
        self.assertEqual( bin2hex('1011'), 'B')

    def test_binary_1010_to_hex(self):
        self.assertEqual( bin2hex('1010'), 'A')

    def test_binary_1001_to_hex(self):
        self.assertEqual( bin2hex('1001'), '9')     

    def test_binary_1000_to_hex(self):
        self.assertEqual( bin2hex('1000'), '8')    

    def test_binary_0111_to_hex(self):
        self.assertEqual( bin2hex('0111'), '7') 

    def test_binary_111_to_hex(self):
        self.assertEqual( bin2hex('111'), '7') 

    def test_binary_0110_to_hex(self):
        self.assertEqual( bin2hex('0110'), '6')  

    def test_binary_110_to_hex(self):
        self.assertEqual( bin2hex('110'), '6')    

    def test_binary_0101_to_hex(self):
        self.assertEqual( bin2hex('0101'), '5')  

    def test_binary_101_to_hex(self):
        self.assertEqual( bin2hex('101'), '5') 

    def test_binary_0100_to_hex(self):
        self.assertEqual( bin2hex('0100'), '4')  

    def test_binary_100_to_hex(self):
        self.assertEqual( bin2hex('100'), '4')  

    def test_binary_0011_to_hex(self):
        self.assertEqual( bin2hex('0011'), '3')  

    def test_binary_011_to_hex(self):
        self.assertEqual( bin2hex('011'), '3')  

    def test_binary_11_to_hex(self):
        self.assertEqual( bin2hex('11'), '3')    

    def test_binary_0010_to_hex(self):
        self.assertEqual( bin2hex('0010'), '2')  

    def test_binary_010_to_hex(self):
        self.assertEqual( bin2hex('010'), '2')  

    def test_binary_10_to_hex(self):
        self.assertEqual( bin2hex('10'), '2')   

    def test_binary_01_to_hex(self):
        self.assertEqual( bin2hex('01'), '1') 

    def test_binary_110100001111_to_hex(self):
        self.assertEqual( bin2hex('110100001111'), 'D0F')   

    def test_binary_0100011111_to_hex(self):
        self.assertEqual( bin2hex('0100011111'), '11F')  

    def test_invalid_binary_A(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('A') 

    def test_invalid_binary_123(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('123')  

    def test_invalid_binary_0101A1000100(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('0101A1000100')  

    def test_invalid_binary_A101100010B(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('A101100010B')  

    def test_invalid_binary_nonalphanumeric(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('!')    

    def test_invalid_binary_nonalphanumeric_in_binary(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('001~') 

    def test_invalid_binary_subtraction(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('0000-1000')            

    def test_invalid_binary_anding(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('0000&1000')   

    def test_invalid_helloWorld_expression(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('hello world')    

    def test_invalid_regexpression(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2hex('[0-1]')                        
    
    
class TestBin2Octal(unittest.TestCase): 
    def test_single_binary_zero(self):
        self.assertEqual( bin2oct('0'), '0')
    def test_single_binary_one(self):
        self.assertEqual( bin2oct('1'), '1')       
    def test_single_binary_triple_zero(self):
        self.assertEqual( bin2oct('000'), '0')    
    def test_single_binary_001(self):
        self.assertEqual( bin2oct('001'), '1') 
    def test_single_binary_010(self):
        self.assertEqual( bin2oct('010'), '2')   
    def test_single_binary_011(self):
        self.assertEqual( bin2oct('011'), '3')                 
    def test_single_binary_100(self):
        self.assertEqual( bin2oct('100'), '4') 
    def test_single_binary_101(self):
        self.assertEqual( bin2oct('101'), '5') 
    def test_single_binary_110(self):
        self.assertEqual( bin2oct('110'), '6') 
    def test_single_binary_111(self):
        self.assertEqual( bin2oct('111'), '7') 
    def test_single_binary_000010(self):
        self.assertEqual( bin2oct('000010'), '02') 
    def test_single_binary_00010(self):
        self.assertEqual( bin2oct('00010'), '02')     
    def test_invalid_binary_A(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('A') 
    def test_invalid_binary_123(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('123')  
    def test_invalid_binary_0101A1000100(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('0101A1000100')  
    def test_invalid_binary_A101100010B(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('A101100010B')  
    def test_invalid_binary_nonalphanumeric(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('!')    
    def test_invalid_binary_nonalphanumeric_in_binary(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('001~') 
    def test_invalid_binary_subtraction(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('0000-1000')            
    def test_invalid_binary_anding(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('0000&1000')   
    def test_invalid_helloWorld_expression(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('hello world')    
    def test_invalid_regexpression(self):
        with self.assertRaises(pi.InvalidBinaryException):
            bin2oct('[0-1]')  

if __name__ == '__main__':
    unittest.main()
