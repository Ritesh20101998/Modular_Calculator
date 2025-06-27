import unittest
import requests
import json

BASE = "http://127.0.0.1:5000"

class TestCalculatorAPI(unittest.TestCase):
    def test_basic_add(self):
        r = requests.post(BASE + "/calculate/basic", json={"operation": "add", "x": 2, "y": 3})
        self.assertEqual(r.status_code, 200)
        self.assertIn("result", r.json())
        self.assertEqual(r.json()["result"], 5)
    def test_basic_invalid(self):
        r = requests.post(BASE + "/calculate/basic", json={"operation": "add", "x": "a", "y": 3})
        self.assertEqual(r.status_code, 400)
    def test_scientific_power(self):
        r = requests.post(BASE + "/calculate/scientific", json={"operation": "power", "x": 2, "y": 8})
        self.assertEqual(r.status_code, 200)
        self.assertIn("result", r.json())
        self.assertEqual(r.json()["result"], 256)
    def test_financial_simple_interest(self):
        r = requests.post(BASE + "/calculate/finance", json={"operation": "simple_interest", "p": 1000, "r": 5, "t": 2})
        self.assertEqual(r.status_code, 200)
        self.assertIn("result", r.json())
        self.assertEqual(r.json()["result"], 100)
    def test_graphical_advanced_formula_safe(self):
        r = requests.post(BASE + "/calculate/graphical/plot", json={"formula": "np.sin(x) + x**2"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers["Content-Type"], "image/png")
    def test_graphical_advanced_formula_unsafe(self):
        r = requests.post(BASE + "/calculate/graphical/plot", json={"formula": "import os; os.system('rm -rf /')"})
        self.assertEqual(r.status_code, 400)
        self.assertIn("error", r.json())
    def test_planning_sip(self):
        r = requests.post(BASE + "/api/planning/sip", json={"monthly_investment": 1000, "annual_rate": 12, "tenure_months": 12})
        self.assertEqual(r.status_code, 200)
        self.assertIn("Maturity Value", r.json())
    def test_planning_rate(self):
        r = requests.post(BASE + "/api/planning/rate", json={"pv": 1000, "pmt": 88.85, "n": 12})
        self.assertEqual(r.status_code, 200)
        self.assertIn("result", r.json())
    def test_test_results_pie_chart(self):
        r = requests.get(BASE + "/test_results/pie_chart")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers["Content-Type"], "image/png")

if __name__ == "__main__":
    unittest.main()
