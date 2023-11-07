#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from methods.patternprinting import print_pyramid
from io import StringIO
import sys
import contextlib 

class TestPrintPyramid(unittest.TestCase):
    @patch('builtins.print')
    def test_patternprinting_numrows_zero_call_print_zero_times(self, mock_print):
        print_pyramid(0, '*')
        self.assertEqual(mock_print.call_count, 0)

    def test_pyramid_pattern_printing_zerorows_asteriks(self):
        expected_output = ''
        
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            print_pyramid(0, "*")
            printed_output = buffer.getvalue()

        self.assertEqual(printed_output, expected_output) 

    @patch('builtins.print')
    def test_patternprinting_numrows_three_call_print_twenty_times(self, mock_print):
        print_pyramid(5, '*')
        self.assertEqual(mock_print.call_count, 20)

    def test_pyramid_pattern_printing_fiverows_asteriks(self):
        expected_output = (
            "*\n"
            "**\n"
            "***\n"
            "****\n"
            "*****\n"
        )
        
        # Assert that the printed output contains the expected parameter
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            print_pyramid(5, "*")
            printed_output = buffer.getvalue()

        self.assertEqual(printed_output, expected_output) 

    @patch('builtins.print')
    def test_patternprinting_numrows_three_call_print_nine_times(self, mock_print):
        print_pyramid(3, '&')
        self.assertEqual(mock_print.call_count, 9)

    def test_pyramid_pattern_printing_fiverows_ampersand(self):
        expected_output = (
            "&\n"
            "&&\n"
            "&&&\n"
        )
        
        # Assert that the printed output contains the expected parameter
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            print_pyramid(3, "&")
            printed_output = buffer.getvalue()

        self.assertEqual(printed_output, expected_output) 

if __name__ == '__main__':
    unittest.main()