"""Tests for Lab 0 Question 1"""

from src.q1 import is_palindrome
import unittest
import sys
sys.path.append(".")


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_true(self) -> None:
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_false(self) -> None:
        self.assertFalse(is_palindrome("Is not a palindrome"))

    def test_empty(self) -> None:
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
