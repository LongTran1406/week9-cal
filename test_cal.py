import pytest
import unittest

from cal import addition, substraction, multiplication, division

def test_addition():
    assert addition(1, 2) == 3
    assert addition(2, 4) == 6

def test_substraction():
    assert substraction(3, 2) == 1
    assert substraction(3, -2) == 5

def test_multiplication():
    assert multiplication(3, 2) == 6
    assert multiplication(3, 0) == 0

def test_division():
    assert division(2, 1) == 2
    with pytest.raises(ValueError):
        division(10, 0)

if __name__ == '__main__':
    unittest.main() 