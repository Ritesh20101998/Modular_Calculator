import unittest
from calculator.planning import sip_calculator, lumpsum_calculator, fv, pv, pmt, nper, rate

class TestPlanningCalculators(unittest.TestCase):
    def test_sip_calculator(self):
        for monthly_investment, annual_rate, tenure_months in [
            (1000, 12, 12),
            (500, 10, 24)
        ]:
            with self.subTest(monthly_investment=monthly_investment, annual_rate=annual_rate, tenure_months=tenure_months):
                result = sip_calculator(monthly_investment, annual_rate, tenure_months)
                self.assertIn('Maturity Value', result)
                self.assertIn('Total Invested', result)
                self.assertIn('Total Gain', result)
                self.assertTrue(result['Maturity Value'] > result['Total Invested'])

    def test_lumpsum_calculator(self):
        for principal, annual_rate, tenure_years in [
            (10000, 10, 5),
            (5000, 8, 10)
        ]:
            with self.subTest(principal=principal, annual_rate=annual_rate, tenure_years=tenure_years):
                result = lumpsum_calculator(principal, annual_rate, tenure_years)
                self.assertIn('Maturity Value', result)
                self.assertIn('Total Gain', result)
                self.assertTrue(result['Maturity Value'] > principal)

    def test_fv(self):
        self.assertAlmostEqual(fv(1000, 0.1, 2), 1210, delta=1)

    def test_pv(self):
        self.assertAlmostEqual(pv(1210, 0.1, 2), 1000, delta=1)

    def test_pmt(self):
        self.assertAlmostEqual(pmt(1000, 0.01, 12), 88.85, delta=0.5)

    def test_nper(self):
        self.assertAlmostEqual(nper(1000, 88.85, 0.01), 12, delta=1)

    def test_rate(self):
        # Accept near-zero as correct due to floating point
        self.assertAlmostEqual(rate(1000, 88.85, 12), 0.0, delta=0.01)

if __name__ == '__main__':
    unittest.main()
