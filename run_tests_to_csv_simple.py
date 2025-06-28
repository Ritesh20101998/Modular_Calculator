import unittest
import csv
import os
from datetime import datetime
import shutil
import coverage

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
    today = datetime.now().strftime('%Y-%m-%d')
    now_time = datetime.now().strftime('%H-%M-%S')
    results_dir = os.path.join('test_results', today)
    os.makedirs(results_dir, exist_ok=True)
    csv_file = os.path.join(results_dir, f'{now_time}_test_results_simple.csv')

    # Start coverage
    cov = coverage.Coverage(source=['calculator', 'api'])
    cov.start()

    loader = unittest.TestLoader()
    suite = loader.discover(test_dir)
    runner = unittest.TextTestRunner(resultclass=CsvTestResultSimple, verbosity=2)
    result = runner.run(suite)

    cov.stop()
    cov.save()
    # Generate HTML report
    cov.html_report(directory=os.path.join(results_dir, 'coverage_html'))
    cov.report()

    # Move or copy other generated files to this folder
    log_file = 'basic.log'
    if os.path.exists(log_file):
        shutil.copy2(log_file, os.path.join(results_dir, f'{now_time}_' + log_file))
    # Add more files as needed

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
    print(f"Coverage HTML report written to {os.path.join(results_dir, 'coverage_html')}")

if __name__ == '__main__':
    run_tests_and_export_to_csv()
