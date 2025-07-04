import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modular_calculator')))
from calculator import basic

class TestBasicCalculator(unittest.TestCase):
    def test_add(self):
        for x, y, expected in [
            (2, 3, 5),
            (-1, 1, 0),
            (1e308, 1e308, float('inf'))
        ]:
            with self.subTest(x=x, y=y, expected=expected):
                self.assertEqual(basic.add(x, y), expected)
    def test_subtract(self):
        for x, y, expected in [
            (5, 3, 2),
            (0, 1, -1)
        ]:
            with self.subTest(x=x, y=y, expected=expected):
                self.assertEqual(basic.subtract(x, y), expected)
    def test_multiply(self):
        for x, y, expected in [
            (2, 3, 6),
            (-1, 1, -1),
            (1e154, 1e154, 1e308)
        ]:
            with self.subTest(x=x, y=y, expected=expected):
                self.assertEqual(basic.multiply(x, y), expected)
    def test_divide(self):
        self.assertEqual(basic.divide(6, 3), 2)
        self.assertEqual(basic.divide(5, 2), 2.5)
        self.assertEqual(basic.divide(5, 0), "Error: Division by zero!")
    def test_modulus(self):
        self.assertEqual(basic.modulus(10, 3), 1)
        self.assertEqual(basic.modulus(10, 0), "Error: Division by zero!")
    def test_floor_divide(self):
        self.assertEqual(basic.floor_divide(10, 3), 3)
        self.assertEqual(basic.floor_divide(10, 0), "Error: Division by zero!")
    def test_power(self):
        self.assertEqual(basic.power(2, 10), 1024)
        self.assertEqual(basic.power(1e154, 2), 1e308)
    def test_max_min_abs(self):
        self.assertEqual(max(10, -5), 10)
        self.assertEqual(min(10, -5), -5)
        self.assertEqual(abs(-123), 123)
    def test_zero_and_negative_inputs(self):
        self.assertEqual(basic.add(0, 0), 0)
        self.assertEqual(basic.subtract(-5, -5), 0)
        self.assertEqual(basic.multiply(0, 100), 0)
        self.assertEqual(basic.divide(0, 1), 0.0)  # Python returns 0.0
        self.assertEqual(basic.divide(-10, 2), -5.0)  # Python returns -5.0
        self.assertEqual(basic.modulus(-10, 3), 2)  # Python: -10 % 3 == 2
        self.assertEqual(basic.floor_divide(-10, 3), -4)
        self.assertEqual(basic.power(-2, 3), -8)
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            basic.add('a', 1)
        with self.assertRaises(TypeError):
            basic.subtract(1, 'b')
        with self.assertRaises(TypeError):
            basic.multiply('x', 'y')
        with self.assertRaises(TypeError):
            basic.divide('x', 2)
        with self.assertRaises(TypeError):
            basic.modulus(1, 'z')
        with self.assertRaises(TypeError):
            basic.floor_divide('foo', 1)
        with self.assertRaises(TypeError):
            basic.power('bar', 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
