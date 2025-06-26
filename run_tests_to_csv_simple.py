import unittest
import csv
import os
from datetime import datetime

class CsvTestResultSimple(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes = []
        self.failures_list = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append((test.id(), 'Success'))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failures_list.append((test.id(), 'Failed'))

    def addError(self, test, err):
        super().addError(test, err)
        self.failures_list.append((test.id(), 'Error'))

def run_tests_and_export_to_csv(test_dir='tests'):
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir)
    runner = unittest.TextTestRunner(resultclass=CsvTestResultSimple, verbosity=2)
    result = runner.run(suite)

    # Create results directory with date and time
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    results_dir = os.path.join('test_results', now)
    os.makedirs(results_dir, exist_ok=True)
    csv_file = os.path.join(results_dir, 'test_results_simple.csv')

    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Test Name', 'Status'])
        # Write successes first
        for test_name, status in result.successes:
            writer.writerow([test_name, status])
        # Write failures and errors after
        for test_name, status in result.failures_list:
            writer.writerow([test_name, status])
    print(f"Test results written to {csv_file}")

if __name__ == '__main__':
    run_tests_and_export_to_csv()
