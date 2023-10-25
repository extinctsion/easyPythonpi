import unittest

# Import the function you want to test
from easyPythonpi.methods.statistics import *

class TestCalculateAverage(unittest.TestCase):
    def test_single_element_list(self):
        result = calculate_average([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_mixed_numbers(self):
        result = calculate_average([-1, 0, 1])
        self.assertEqual(result, 0.0)

    def test_negative_numbers(self):
        result = calculate_average([-5, -3, -1])
        self.assertEqual(result, -3.0)

    def test_decimal_numbers(self):
        result = calculate_average([0.5, 1.5, 2.5])
        self.assertEqual(result, 1.5)

if __name__ == '__main__':
    unittest.main()
