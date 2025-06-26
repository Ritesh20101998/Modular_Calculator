import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modular_calculator')))

import unittest
from calculator import scientific

class TestScientificCalculator(unittest.TestCase):
    def test_power(self):
        self.assertEqual(scientific.power(2, 3), 8)
    def test_sqrt(self):
        self.assertEqual(scientific.sqrt(9), 3)
        with self.assertRaises(ValueError):
            scientific.sqrt(-1)
    def test_sine(self):
        self.assertAlmostEqual(scientific.sine(90), 1.0, places=3)
    def test_cosine(self):
        self.assertAlmostEqual(scientific.cosine(0), 1.0, places=3)
    def test_tangent(self):
        self.assertAlmostEqual(scientific.tangent(45), 1.0, places=3)
    def test_log_exp(self):
        import math
        self.assertAlmostEqual(scientific.log(10), math.log(10), places=6)
        self.assertAlmostEqual(scientific.exp(2), math.exp(2), places=6)
        with self.assertRaises(ValueError):
            scientific.log(-1)
    def test_trig_edge_cases(self):
        self.assertAlmostEqual(scientific.sine(0), 0.0, places=6)
        self.assertAlmostEqual(scientific.cosine(180), -1.0, places=6)
        self.assertAlmostEqual(scientific.tangent(0), 0.0, places=6)
    def test_large_and_small_numbers(self):
        self.assertAlmostEqual(scientific.sqrt(1e-10), 1e-5, places=10)
        self.assertAlmostEqual(scientific.power(1e5, 2), 1e10, places=2)
        self.assertAlmostEqual(scientific.exp(0), 1.0, places=6)
        self.assertAlmostEqual(scientific.log(1), 0.0, places=6)
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            scientific.sqrt('a')
        with self.assertRaises(ValueError):
            scientific.power('a', 2)
    def test_nan_and_inf(self):
        import math
        self.assertTrue(math.isnan(scientific.sine(float('nan'))))
        self.assertTrue(math.isnan(scientific.cosine(float('nan'))))
        self.assertTrue(math.isnan(scientific.tangent(float('nan'))))
        self.assertTrue(math.isinf(scientific.power(1e308, 2)))
    def test_log_base(self):
        self.assertAlmostEqual(scientific.log(100, 10), 2.0, places=6)
        with self.assertRaises(ValueError):
            scientific.log(0, 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
