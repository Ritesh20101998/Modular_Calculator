import unittest
from calculator import basic, scientific, financial
import os

class EmojiTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_statuses = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_statuses.append((test, True))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_statuses.append((test, False))

    def addError(self, test, err):
        super().addError(test, err)
        self.test_statuses.append((test, False))

    def printEmojiSummary(self):
        print("\nTest Results Summary:")
        for test, passed in self.test_statuses:
            emoji = '🟢' if passed else '🔴'
            print(f"{emoji} {test._testMethodName}")

class EmojiTestRunner(unittest.TextTestRunner):
    resultclass = EmojiTestResult
    def run(self, test):
        result = super().run(test)
        result.printEmojiSummary()
        return result

class TestBasicCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(2, 3), 5)
        self.assertEqual(basic.add(-1, 1), 0)
        self.assertEqual(basic.add(1e308, 1e308), float('inf'))
    def test_subtract(self):
        self.assertEqual(basic.subtract(5, 3), 2)
        self.assertEqual(basic.subtract(0, 1), -1)
    def test_multiply(self):
        self.assertEqual(basic.multiply(2, 3), 6)
        self.assertEqual(basic.multiply(-1, 1), -1)
        self.assertEqual(basic.multiply(1e154, 1e154), float('inf'))
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
        self.assertEqual(basic.power(1e154, 2), float('inf'))
    def test_max_min_abs(self):
        self.assertEqual(max(10, -5), 10)
        self.assertEqual(min(10, -5), -5)
        self.assertEqual(abs(-123), 123)
    def test_zero_and_negative_inputs(self):
        self.assertEqual(basic.add(0, 0), 0)
        self.assertEqual(basic.subtract(-5, -5), 0)
        self.assertEqual(basic.multiply(0, 100), 0)
        self.assertEqual(basic.divide(0, 1), 0)
        self.assertEqual(basic.divide(-10, 2), -5)
        self.assertEqual(basic.modulus(-10, 3), -1)
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

class TestFinancialCalculator(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(financial.simple_interest(1000, 5, 2), 100)
    def test_compound_interest(self):
        result = financial.compound_interest(1000, 10, 2, 1)
        self.assertAlmostEqual(result, 210, delta=1)
    def test_risk_return_analysis(self):
        returns = [0.1, 0.2, 0.15, 0.18]
        result = financial.risk_return_analysis(returns)
        self.assertIn('mean_return', result)
        self.assertIn('stddev', result)
    def test_format_currency(self):
        self.assertEqual(financial.format_currency(1234.567, 'USD'), 'USD 1,234.57')
    def test_read_financial_data_csv(self):
        import pandas as pd
        df = pd.DataFrame({'a':[1,2],'b':[3,4]})
        df.to_csv('test.csv', index=False)
        records = financial.read_financial_data_csv('test.csv')
        self.assertEqual(len(records), 2)
        os.remove('test.csv')
    def test_read_financial_data_excel(self):
        import pandas as pd
        df = pd.DataFrame({'a':[1,2],'b':[3,4]})
        df.to_excel('test.xlsx', index=False)
        records = financial.read_financial_data_excel('test.xlsx')
        self.assertEqual(len(records), 2)
        os.remove('test.xlsx')
    def test_save_financial_record(self):
        db_path = 'test_finance.db'
        import sqlite3
        conn = sqlite3.connect(db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS test (a INTEGER, b INTEGER)')
        conn.close()
        financial.save_financial_record(db_path, 'test', {'a': 1, 'b': 2})
        conn = sqlite3.connect(db_path)
        cursor = conn.execute('SELECT * FROM test')
        row = cursor.fetchone()
        self.assertEqual(row, (1, 2))
        conn.close()
        os.remove(db_path)
    def test_compound_interest_high_frequency(self):
        # Test with high compounding frequency
        result = financial.compound_interest(1000, 5, 10, 365)  # daily compounding
        self.assertTrue(result > 1600)
    def test_format_currency_large(self):
        self.assertEqual(financial.format_currency(123456789.987, 'EUR'), 'EUR 123,456,789.99')
    def test_risk_return_analysis_empty(self):
        with self.assertRaises(ValueError):
            financial.risk_return_analysis([])
    def test_negative_and_zero_principal(self):
        self.assertEqual(financial.simple_interest(0, 5, 2), 0)
        self.assertEqual(financial.simple_interest(-1000, 5, 2), -100)
        self.assertAlmostEqual(financial.compound_interest(0, 10, 2, 1), 0)
        self.assertAlmostEqual(financial.compound_interest(-1000, 10, 2, 1), -210, delta=1)
    def test_currency_formatting_symbols(self):
        self.assertEqual(financial.format_currency(1000, '$'), '$ 1,000.00')
        self.assertEqual(financial.format_currency(1000, '₹'), '₹ 1,000.00')
    def test_invalid_currency_format(self):
        with self.assertRaises(Exception):
            financial.format_currency('notanumber', 'USD')
    def test_db_error_handling(self):
        # Try saving to a non-existent table
        with self.assertRaises(Exception):
            financial.save_financial_record('nonexistent.db', 'no_table', {'a': 1})

class TestGraphicalCalculator(unittest.TestCase):
    def test_plot_y_equals_x_squared(self):
        # Should not raise exception
        try:
            from calculator import graphical
            graphical.plot_y_equals_x_squared()
            passed = True
        except Exception:
            passed = False
        self.assertTrue(passed)
    def test_plot_y_equals_x_squared_image(self):
        from calculator import graphical
        img = graphical.plot_y_equals_x_squared()
        self.assertIsNotNone(img)
        # Optionally check if img is a matplotlib Figure or BytesIO
        import io
        self.assertTrue(isinstance(img, io.BytesIO) or hasattr(img, 'savefig'))
    def test_plot_y_equals_x_squared_type(self):
        from calculator import graphical
        img = graphical.plot_y_equals_x_squared()
        import io
        self.assertTrue(isinstance(img, io.BytesIO) or hasattr(img, 'savefig'))
    def test_plot_y_equals_x_squared_exception(self):
        from calculator import graphical
        import numpy as np
        # Patch np.linspace to raise exception
        orig_linspace = np.linspace
        np.linspace = lambda *a, **k: (_ for _ in ()).throw(ValueError('Test error'))
        try:
            with self.assertRaises(Exception):
                graphical.plot_y_equals_x_squared()
        finally:
            np.linspace = orig_linspace

if __name__ == "__main__":
    unittest.main(testRunner=EmojiTestRunner(), verbosity=2)
