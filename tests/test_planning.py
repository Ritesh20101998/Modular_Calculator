import unittest
from calculator.planning import sip_calculator, lumpsum_calculator, fv, pv, pmt, nper, rate

class TestPlanningCalculators(unittest.TestCase):
    def test_sip_calculator(self):
        result = sip_calculator(1000, 12, 12)
        self.assertIn('Maturity Value', result)
        self.assertIn('Total Invested', result)
        self.assertIn('Total Gain', result)
        self.assertTrue(result['Maturity Value'] > result['Total Invested'])

    def test_lumpsum_calculator(self):
        result = lumpsum_calculator(10000, 10, 5)
        self.assertIn('Maturity Value', result)
        self.assertIn('Total Gain', result)
        self.assertTrue(result['Maturity Value'] > 10000)

    def test_fv(self):
        self.assertAlmostEqual(fv(1000, 0.1, 2), 1210, delta=1)

    def test_pv(self):
        self.assertAlmostEqual(pv(1210, 0.1, 2), 1000, delta=1)

    def test_pmt(self):
        self.assertAlmostEqual(pmt(1000, 0.01, 12), 88.85, delta=0.5)

    def test_nper(self):
        self.assertAlmostEqual(nper(1000, 88.85, 0.01), 12, delta=1)

    def test_rate(self):
        self.assertAlmostEqual(rate(1000, 88.85, 12), 0.01, delta=0.01)

if __name__ == '__main__':
    unittest.main()
