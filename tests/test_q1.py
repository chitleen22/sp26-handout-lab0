"""Tests for Lab 0 Question 1"""

from src.q1 import is_palindrome
import unittest
import sys
sys.path.append(".")


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_True(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_case_insensetive(self):
        self.assertTrue( is .is_palindrome("RaCeCaR"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("taco cat"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("yellow"))


if __name__ == "__main__":
    unittest.main()
