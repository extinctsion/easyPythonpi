import unittest
import easyPythonpi

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(easyPythonpi.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(easyPythonpi.add(-1, 1), 0)

    def test_add_with_zero(self):
        self.assertEqual(easyPythonpi.add(0.5, 0.5), 1.0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(easyPythonpi.sub(5, 2), 3)

    def test_subtract_with_zero(self):
        self.assertEqual(easyPythonpi.sub(0, 0), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(easyPythonpi.sub(-1, -1), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(easyPythonpi.multi(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(easyPythonpi.multi(0, 5), 0)

    def test_multiply_by_negative_numbers(self):
        self.assertEqual(easyPythonpi.multi(-2, 6), -12)

    def test_divide_by_smaller_number(self):
        self.assertEqual(easyPythonpi.div(6, 2), 3.0)

    def test_divide_zero_by_number(self):
        self.assertEqual(easyPythonpi.div(0, 5), 0.0)

    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            easyPythonpi.div(5, 0)

    def test_mod_positive_numbers(self):
        self.assertEqual(easyPythonpi.mod(7, 3), 1)
        self.assertEqual(easyPythonpi.mod(10, 2), 0)

    def test_mod_zero(self):
        self.assertEqual(easyPythonpi.mod(0, 5), 0)

    def test_mod_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            easyPythonpi.mod(8, 0)


if __name__ == '__main__':
    unittest.main()