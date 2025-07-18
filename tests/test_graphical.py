import sys
import os
import unittest
from calculator import graphical
import io
import numpy as np

class TestGraphicalCalculator(unittest.TestCase):
    def test_plot_y_equals_x_squared(self):
        for _ in range(2):  # Run twice to check for state issues
            with self.subTest(run=_):
                try:
                    graphical.plot_y_equals_x_squared()
                    passed = True
                except Exception:
                    passed = False
                self.assertTrue(passed)
    def test_plot_y_equals_x_squared_image(self):
        img = graphical.plot_y_equals_x_squared()
        self.assertIsNotNone(img)
        self.assertTrue(isinstance(img, io.BytesIO) or hasattr(img, 'savefig'))
    def test_plot_y_equals_x_squared_type(self):
        img = graphical.plot_y_equals_x_squared()
        self.assertTrue(isinstance(img, io.BytesIO) or hasattr(img, 'savefig'))
    def test_plot_y_equals_x_squared_exception(self):
        # Patch np.linspace to raise exception
        orig_linspace = np.linspace
        np.linspace = lambda *a, **k: (_ for _ in ()).throw(ValueError('Test error'))
        try:
            with self.assertRaises(Exception):
                graphical.plot_y_equals_x_squared()
        finally:
            np.linspace = orig_linspace

if __name__ == "__main__":
    unittest.main(verbosity=2)
