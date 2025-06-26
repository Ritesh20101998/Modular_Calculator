import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modular_calculator')))

import unittest
from calculator.finance import finance

class TestFinancialCalculator(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(finance.simple_interest(1000, 5, 2), 100)
    def test_compound_interest(self):
        result = finance.compound_interest(1000, 10, 2, 1)
        self.assertAlmostEqual(result, 210, delta=1)
    def test_risk_return_analysis(self):
        returns = [0.1, 0.2, 0.15, 0.18]
        result = finance.risk_return_analysis(returns)
        self.assertIn('mean_return', result)
        self.assertIn('stddev', result)
    def test_format_currency(self):
        self.assertEqual(finance.format_currency(1234.567, 'USD'), 'USD 1,234.57')
    def test_read_financial_data_csv(self):
        import pandas as pd
        df = pd.DataFrame({'a':[1,2],'b':[3,4]})
        df.to_csv('test.csv', index=False)
        records = finance.read_financial_data_csv('test.csv')
        self.assertEqual(len(records), 2)
        os.remove('test.csv')
    def test_read_financial_data_excel(self):
        import pandas as pd
        df = pd.DataFrame({'a':[1,2],'b':[3,4]})
        df.to_excel('test.xlsx', index=False)
        records = finance.read_financial_data_excel('test.xlsx')
        self.assertEqual(len(records), 2)
        os.remove('test.xlsx')
    def test_save_financial_record(self):
        db_path = 'test_finance.db'
        import sqlite3
        conn = sqlite3.connect(db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS test (a INTEGER, b INTEGER)')
        conn.close()
        finance.save_financial_record(db_path, 'test', {'a': 1, 'b': 2})
        conn = sqlite3.connect(db_path)
        cursor = conn.execute('SELECT * FROM test')
        row = cursor.fetchone()
        self.assertEqual(row, (1, 2))
        conn.close()
        os.remove(db_path)
    def test_compound_interest_high_frequency(self):
        # Test with high compounding frequency
        result = finance.compound_interest(1000, 5, 10, 365)  # daily compounding
        self.assertTrue(result > 1600)
    def test_format_currency_large(self):
        self.assertEqual(finance.format_currency(123456789.987, 'EUR'), 'EUR 123,456,789.99')
    def test_risk_return_analysis_empty(self):
        with self.assertRaises(ValueError):
            finance.risk_return_analysis([])
    def test_negative_and_zero_principal(self):
        self.assertEqual(finance.simple_interest(0, 5, 2), 0)
        self.assertEqual(finance.simple_interest(-1000, 5, 2), -100)
        self.assertAlmostEqual(finance.compound_interest(0, 10, 2, 1), 0)
        self.assertAlmostEqual(finance.compound_interest(-1000, 10, 2, 1), -210, delta=1)
    def test_currency_formatting_symbols(self):
        self.assertEqual(finance.format_currency(1000, '$'), '$ 1,000.00')
        self.assertEqual(finance.format_currency(1000, '₹'), '₹ 1,000.00')
    def test_invalid_currency_format(self):
        with self.assertRaises(Exception):
            finance.format_currency('notanumber', 'USD')
    def test_db_error_handling(self):
        # Try saving to a non-existent table
        with self.assertRaises(Exception):
            finance.save_financial_record('nonexistent.db', 'no_table', {'a': 1})

if __name__ == "__main__":
    unittest.main(verbosity=2)
