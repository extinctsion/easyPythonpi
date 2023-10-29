import unittest

# Import the function you want to test
from methods.stringmainpulation import *

class TestStringManipulation(unittest.TestCase):
    def test_count_vowels_string_no_vowels(self):
        result = count_vowels("rhythm")
        self.assertEqual(result, {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test_count_vowels_string_has_vowels(self):
        result = count_vowels("aeiouAEIOU")
        self.assertEqual(result, {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2})

    def test_count_vowels_string_vowels_and_consonants(self):
        result = count_vowels("Hello, World!")
        self.assertEqual(result, {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})

    def test_count_vowels_empty_string(self):
        result = count_vowels("")
        self.assertEqual(result, {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test_count_vowels_empty_string(self):
        result = count_vowels("Python Is Awesome")
        self.assertEqual(result, {'a': 1, 'e': 2, 'i': 1, 'o': 2, 'u': 0})

    def test_count_vowels_string_non_ascii_chars_only(self):
        result = count_vowels("#!@$% ?")
        self.assertEqual(result, {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test_is_palindrome_empty_string(self):
        result = is_palindrome("")
        self.assertTrue(result)

    def test_is_palindrome_whitespace_only(self):
        result = is_palindrome(" ")
        self.assertTrue(result)

    def test_is_palindrome_single_character(self):
        result = is_palindrome("a")
        self.assertTrue(result)

    def test_is_palindrome_sentence_without_punctuation(self):
        result = is_palindrome("A man a plan a canal Panama")
        self.assertTrue(result)

    def test_is_palindrome_sentence_with_punctuation(self):
        result = is_palindrome("Was it a car or a cat I saw?")
        self.assertTrue(result)

    def test_is_palindrome_sentence_not_palindrome(self):
        result = is_palindrome("Hello, World!")
        self.assertFalse(result)    

    def test_remove_punctuation_empty_string_remove_punctuation(self):
        result = remove_punctuation("")
        self.assertEqual(result, "")

    def test_remove_punctuation_sentence_no_punctuation(self):
        result = remove_punctuation("This is a test string")
        self.assertEqual(result, "This is a test string")

    def test_remove_punctuation_sentence_with_punctuation(self):
        result = remove_punctuation("Hello, World! This is a test.")
        self.assertEqual(result, "Hello World This is a test")

    def test_remove_punctuation_mixed_characters(self):
        result = remove_punctuation("123@abc#def%")
        self.assertEqual(result, "123abcdef")

if __name__ == '__main__':
    unittest.main()
