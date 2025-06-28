import unittest
import requests
import csv
import os
from datetime import datetime

# --- CONFIG ---
API_BASE = "http://127.0.0.1:5000"
API_PERF_TESTS = [
    ("POST", "/calculate/basic", {"operation": "add", "x": 2, "y": 3}),
    ("POST", "/calculate/basic", {"operation": "add", "x": "a", "y": 3}),
    ("POST", "/calculate/scientific", {"operation": "power", "x": 2, "y": 8}),
    ("POST", "/calculate/finance", {"operation": "simple_interest", "p": 1000, "r": 5, "t": 2}),
    ("POST", "/calculate/graphical/plot", {"formula": "np.sin(x) + x**2"}),
    ("POST", "/calculate/graphical/plot", {"formula": "import os; os.system('rm -rf /')"}),
    ("POST", "/api/planning/sip", {"monthly_investment": 1000, "annual_rate": 12, "tenure_months": 12}),
    ("POST", "/api/planning/rate", {"pv": 1000, "pmt": 88.85, "n": 12}),
    ("GET", "/test_results/pie_chart", None),
]
UNITTEST_MODULES = [
    "tests.test_basic",
    "tests.test_financial",
    "tests.test_graphical",
    "tests.test_planning",
    "tests.test_scientific",
    "tests.test_api"
]
RESULTS_DIR = os.path.join("test_results", datetime.now().strftime("%Y-%m-%d"))
os.makedirs(RESULTS_DIR, exist_ok=True)
RESULTS_FILE = os.path.join(RESULTS_DIR, f"combined_results_{datetime.now().strftime('%H%M%S')}.csv")

# --- UNITTEST RUNNER ---
def run_unittests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for mod in UNITTEST_MODULES:
        try:
            suite.addTests(loader.loadTestsFromName(mod))
        except Exception as e:
            print(f"Could not load {mod}: {e}")
    results = []
    class CSVTestResult(unittest.TextTestResult):
        def addSuccess(self, test):
            super().addSuccess(test)
            results.append({
                'Test Name': str(test),
                'Status': 'PASS',
                'Type': 'unit',
                'Details': ''
            })
        def addFailure(self, test, err):
            super().addFailure(test, err)
            results.append({
                'Test Name': str(test),
                'Status': 'FAIL',
                'Type': 'unit',
                'Details': self._exc_info_to_string(err, test)
            })
        def addError(self, test, err):
            super().addError(test, err)
            results.append({
                'Test Name': str(test),
                'Status': 'ERROR',
                'Type': 'unit',
                'Details': self._exc_info_to_string(err, test)
            })
    runner = unittest.TextTestRunner(resultclass=CSVTestResult, verbosity=2)
    runner.run(suite)
    return results

# --- API TESTS (no performance) ---
def run_api_tests():
    results = []
    for method, route, payload in API_PERF_TESTS:
        url = API_BASE + route
        test_name = f"API {method} {route}"
        try:
            if method == "POST":
                r = requests.post(url, json=payload)
            else:
                r = requests.get(url)
            status = 'PASS' if r.status_code in (200, 400) else 'FAIL'
            details = '' if status == 'PASS' else f"Status code: {r.status_code}, Response: {r.text}"
            results.append({
                'Test Name': test_name,
                'Status': status,
                'Type': 'api',
                'Details': details
            })
        except Exception as e:
            results.append({
                'Test Name': test_name,
                'Status': 'ERROR',
                'Type': 'api',
                'Details': str(e)
            })
    return results

# --- MAIN ---
if __name__ == "__main__":
    all_results = []
    print("Running unit tests...")
    all_results.extend(run_unittests())
    print("Running API tests...")
    all_results.extend(run_api_tests())
    print(f"Writing results to {RESULTS_FILE}")
    with open(RESULTS_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Test Name', 'Status', 'Type', 'Details'])
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)
    print("Done.")
