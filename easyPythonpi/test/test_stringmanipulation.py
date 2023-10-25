import unittest

# Import the function you want to test
from easyPythonpi.methods.stringmainpulation import *


class TestCountVowels(unittest.TestCase):
    def test_no_vowels(self):
        result = count_vowels("rhythm")
        self.assertEqual(result, {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0})

    def test_all_vowels(self):
        result = count_vowels("aeiouAEIOU")
        self.assertEqual(result, {"a": 2, "e": 2, "i": 2, "o": 2, "u": 2})

    def test_mixed_string(self):
        result = count_vowels("Hello, World!")
        self.assertEqual(result, {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0})

    def test_empty_string_counting_vowels(self):
        result = count_vowels("")
        self.assertEqual(result, {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0})

    def test_case_insensitive(self):
        result = count_vowels("Python Is Awesome")
        self.assertEqual(result, {"a": 1, "e": 2, "i": 1, "o": 2, "u": 0})

    def test_empty_string(self):
        result = ispalindrome("")
        self.assertTrue(result)

    def test_single_character(self):
        result = ispalindrome("a")
        self.assertTrue(result)

    def test_palindrome_with_spaces(self):
        s = "A man a Plan a canal PanamA"
        s = remove_spaces(s)
        result = ispalindrome(s)
        self.assertTrue(result)

    def test_palindrome_with_punctuation(self):
        s = "Was it a car or a cat I saw?"
        s = remove_punctuation(s)
        s = remove_spaces(s) 
        s = s.lower()
        result = ispalindrome(s)
        self.assertTrue(result)

    def test_non_palindrome(self):
        result = ispalindrome("Hello, World!")
        self.assertFalse(result)

    def test_empty_string_remove_punctuation(self):
        result = remove_punctuation("")
        self.assertEqual(result, "")

    def test_no_punctuation(self):
        result = remove_punctuation("This is a test string")
        self.assertEqual(result, "This is a test string")

    def test_with_punctuation(self):
        result = remove_punctuation("Hello, World! This is a test.")
        self.assertEqual(result, "Hello World This is a test")

    def test_mixed_characters(self):
        result = remove_punctuation("123@abc#def%")
        self.assertEqual(result, "123abcdef")

    def test_unicode_punctuation(self):
        result = remove_punctuation("Unicode — string: ™ ©")
        self.assertEqual(result, "Unicode  string  ")


if __name__ == "__main__":
    unittest.main()
