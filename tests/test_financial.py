import sys
import os
import unittest
from calculator import finance

class TestFinancialCalculator(unittest.TestCase):
    def test_simple_interest(self):
        for p, r, t, expected in [
            (1000, 5, 2, 100),
            (2000, 3, 1, 60)
        ]:
            with self.subTest(p=p, r=r, t=t, expected=expected):
                self.assertEqual(finance.simple_interest(p, r, t), expected)
    def test_compound_interest(self):
        for p, r, t, n, expected in [
            (1000, 10, 2, 1, 210),
            (500, 5, 3, 2, 79)
        ]:
            with self.subTest(p=p, r=r, t=t, n=n, expected=expected):
                result = finance.compound_interest(p, r, t, n)
                self.assertAlmostEqual(result, expected, delta=2)
    def test_risk_return_analysis(self):
        returns = [0.1, 0.2, 0.15, 0.18]
        result = finance.risk_return_analysis(returns)
        self.assertIn('mean_return', result)
        self.assertIn('stddev', result)
    def test_format_currency(self):
        for val, curr, expected in [
            (1234.567, 'USD', 'USD 1,234.57'),
            (1000, 'INR', 'INR 1,000.00')
        ]:
            with self.subTest(val=val, curr=curr):
                self.assertEqual(finance.format_currency(val, curr), expected)
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
        self.assertTrue(result > 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
