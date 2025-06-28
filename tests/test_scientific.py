import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modular_calculator')))

from calculator import scientific

class TestScientificCalculator(unittest.TestCase):
    def test_power(self):
        for base, exp, expected in [
            (2, 3, 8),
            (10, 2, 100),
            (5, 0, 1)
        ]:
            with self.subTest(base=base, exp=exp):
                self.assertEqual(scientific.power(base, exp), expected)
    def test_sqrt(self):
        for val, expected in [
            (9, 3),
            (16, 4),
            (1e-10, 1e-5)
        ]:
            with self.subTest(val=val):
                self.assertAlmostEqual(scientific.sqrt(val), expected, places=6)
        with self.assertRaises(ValueError):
            scientific.sqrt(-1)
        with self.assertRaises(ValueError):
            scientific.sqrt('a')
    def test_sine(self):
        for angle, expected in [
            (90, 1.0),
            (0, 0.0)
        ]:
            with self.subTest(angle=angle):
                self.assertAlmostEqual(scientific.sine(angle), expected, places=3)
    def test_cosine(self):
        for angle, expected in [
            (0, 1.0),
            (180, -1.0)
        ]:
            with self.subTest(angle=angle):
                self.assertAlmostEqual(scientific.cosine(angle), expected, places=3)
    def test_tangent(self):
        for angle, expected in [
            (45, 1.0),
            (0, 0.0)
        ]:
            with self.subTest(angle=angle):
                self.assertAlmostEqual(scientific.tangent(angle), expected, places=3)
    def test_log_exp(self):
        import math
        for val, expected in [
            (10, math.log(10)),
            (1, 0.0)
        ]:
            with self.subTest(val=val):
                self.assertAlmostEqual(scientific.log(val), expected, places=6)
        for val, expected in [
            (2, math.exp(2)),
            (0, 1.0)
        ]:
            with self.subTest(val=val):
                self.assertAlmostEqual(scientific.exp(val), expected, places=6)
        with self.assertRaises(ValueError):
            scientific.log(-1)
    def test_trig_edge_cases(self):
        for func, arg, expected in [
            (scientific.sine, 0, 0.0),
            (scientific.cosine, 180, -1.0),
            (scientific.tangent, 0, 0.0)
        ]:
            with self.subTest(func=func.__name__, arg=arg):
                self.assertAlmostEqual(func(arg), expected, places=6)
    def test_large_and_small_numbers(self):
        for func, args, expected, places in [
            (scientific.sqrt, (1e-10,), 1e-5, 10),
            (scientific.power, (1e5, 2), 1e10, 2),
            (scientific.exp, (0,), 1.0, 6),
            (scientific.log, (1,), 0.0, 6)
        ]:
            with self.subTest(func=func.__name__, args=args):
                self.assertAlmostEqual(func(*args), expected, places=places)
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            scientific.sqrt('a')
        with self.assertRaises(ValueError):
            scientific.power('a', 2)
    def test_nan_and_inf(self):
        import math
        for func in [scientific.sine, scientific.cosine, scientific.tangent]:
            with self.subTest(func=func.__name__):
                self.assertTrue(math.isnan(func(float('nan'))))
        # Python raises OverflowError for 1e308**2
        with self.assertRaises(OverflowError):
            scientific.power(1e308, 2)
    def test_log_base(self):
        for val, base, expected in [
            (100, 10, 2.0)
        ]:
            with self.subTest(val=val, base=base):
                self.assertAlmostEqual(scientific.log(val, base), expected, places=6)
        with self.assertRaises(ValueError):
            scientific.log(0, 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
