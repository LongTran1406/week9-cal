import pytest
import unittest

from cal import addition, substraction, multiplication, division

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 2), 3)
        self.assertEqual(addition(1, 3), 4)

    def test_substraction(self):
        self.assertEqual(substraction(3, 2), 1)


    def test_multiplication(self):
        self.assertEqual(multiplication(3, 2), 6)


    def test_division(self):
        self.assertEqual(division(-1, -1), 1)
        with self.assertRaises(ValueError):
            division(1, 0)

if __name__ == '__main__':
    unittest.main() 