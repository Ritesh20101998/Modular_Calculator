# Python Modular Calculator

![Advanced Graphical Calculator Example](docs/images/advanced_graphical_example.png)

A robust, modular calculator project in Python supporting Basic, Scientific, Financial, Graphical, and Planning calculations. Includes a REST API, logging, error handling, and unit tests.

## Features
- **Basic Calculator:** Addition, subtraction, multiplication, division, modulus, floor division, power, max, min, abs.
- **Scientific Calculator:** Power, square root, sine, cosine, tangent, log, exp, advanced error handling.
- **Financial Calculator:** Simple/compound interest, risk & return analysis, currency formatting, CSV/Excel/SQLite support, robust error handling.
- **Graphical Calculator:** Plots (e.g., y = x²) as PNG images via API, extensible for more plots.
- **Advanced Graphical Calculator:** Plot any mathematical function by providing a formula string (e.g., `y = np.sin(x) + x**2`).
  - New API endpoint: `/calculate/graphical/plot` (POST: `{ "formula": "np.sin(x) + x**2" }`)
  - Returns a PNG image of the plotted function.
  - Supports all numpy functions and vectorized math.
- **Planning Calculator:** SIP calculator, Lumpsum calculator, Time Value of Money (FV, PV, PMT, N, Rate) with robust error handling and logging.
- **REST API:** Endpoints for all calculator types using Flask, with clear JSON input/output.
- **Logging:** Structured logs for all operations and errors, per-module log files in `logs/`.
- **Unit Tests:** Full coverage with advanced and edge cases, emoji-based summary for quick review.
- **User-friendly error messages and install instructions for missing packages.**
- **Modular, extensible codebase:** Easy to add new features or modules.
- **Comprehensive documentation:** For users and developers.

## Requirements
- Python 3.8+
- Flask
- pandas
- matplotlib
- numpy

Install dependencies:
```
pip install flask pandas matplotlib numpy
```

## Usage
### Run the API
```
python api/calculator_api.py
```

### Run Unit Tests
```
python -m unittest -v tests/test_calculator.py
```

### Example API Request (Basic Addition)
```
curl -X POST http://127.0.0.1:5000/calculate/basic -H "Content-Type: application/json" -d '{"operation": "add", "x": 2, "y": 3}'
```

### Graphical API Example
```
curl -X POST http://127.0.0.1:5000/calculate/graphical -H "Content-Type: application/json" -d '{"operation": "plot_y_equals_x_squared"}' --output plot.png
```

### Advanced Graphical API Example (Custom Formula)
```
curl -X POST http://127.0.0.1:5000/calculate/graphical/plot -H "Content-Type: application/json" -d '{"formula": "np.sin(x) + x**2"}' --output custom_plot.png
```

### Planning API Example (SIP Calculator)
```
curl -X POST http://127.0.0.1:5000/api/planning/sip -H "Content-Type: application/json" -d '{"monthly_investment": 100, "annual_rate": 5, "tenure_months": 60}'
```

## API Endpoints
- `/calculate/basic` — Basic operations (add, subtract, multiply, divide, modulus, floor_divide, power, max, min, abs)
- `/calculate/scientific` — Scientific operations (power, sqrt, sine, cosine, tangent, log, exp)
- `/calculate/finance` — Financial operations (simple_interest, compound_interest, risk_return_analysis, format_currency, data import/export)
- `/calculate/graphical` — Graphical operations (e.g., plot_y_equals_x_squared)
- `/calculate/graphical/plot` — Advanced graphical operation (POST: formula string for custom plot)
- `/api/planning/sip` — SIP calculator (POST: monthly_investment, annual_rate, tenure_months)
- `/api/planning/lumpsum` — Lumpsum calculator (POST: principal, annual_rate, tenure_years)
- `/api/planning/tvm` — Time Value of Money (POST: operation, and required parameters for FV, PV, PMT, N, Rate)

All endpoints accept POST requests with JSON payloads. See code and tests for details.

## Project Structure
- `calculator/` — All calculator modules (basic, scientific, financial, graphical, planning)
- `api/` — Flask API
- `tests/` — Unit tests
- `logs/` — Log files (ignored by git)
- `README.md` — Project documentation
- `.gitignore` — Git ignore rules

## Logging
- Logs for each module are stored in `logs/`.
- Log files are ignored by git.
- Useful for debugging and auditing.

## Error Handling
- All modules and API endpoints provide user-friendly error messages.
- If a required package is missing, a clear install instruction is shown.
- Defensive coding for invalid input, division by zero, file/database errors, etc.

## New Features (June 26, 2025)

- **Automated Test Result Export:**
  - Added a script (`run_tests_to_csv_simple.py`) to run all unit tests and export results to a CSV file.
  - Test results are now saved in a timestamped folder under `test_results/`, with all successes listed first, followed by failures and errors.
  - This makes it easy to track test runs and share results.

- **Improved Test and API Compatibility:**
  - Refactored core modules (`basic.py`, `scientific.py`, `graphical.py`, `finance.py`) for better compatibility with tests and API endpoints.
  - Added type and domain checks to all calculator functions for robust error handling and clearer test results.

- **Graphical API and Module:**
  - The graphical calculator now returns plots as image buffers, supporting both API and test automation.

- **Test Results Organization:**
  - Test results are now separated by status (successes first, then failures/errors) in the CSV output for easier review.

---

## 📖 Instructions & Feature Guide (Summary)

This project is a modular, extensible Python calculator with REST API and optional frontend. It supports:
- **Basic operations:** add, subtract, multiply, divide, modulus, floor division, power, max, min, abs
- **Scientific functions:** power, sqrt, sine, cosine, tangent, log, exp
- **Financial calculations:** simple/compound interest, and more
- **Graphical plotting:** e.g., y = x² (returns PNG image)

### How it works
- Each module (`basic.py`, `scientific.py`, `financial.py`, `graphical.py`) defines calculator functions.
- API modules (e.g., `basic_api.py`) expose these via HTTP POST endpoints.
- You can use the API by sending JSON requests, or import modules directly in Python.

### Example API Usage
- POST to `/calculate/basic` with `{ "operation": "add", "x": 2, "y": 3 }`
- See [INSTRUCTIONS.md](INSTRUCTIONS.md) for all endpoints and usage examples.

### Error Handling
- All functions check for invalid input and return clear error messages.
- Division by zero and domain errors are handled gracefully.

### Extending the Calculator
- Add new functions to the relevant module.
- Add/extend API endpoints.
- Add tests in the `tests/` directory.

---

## 📁 Project Directory Structure

```
Modular_Calculator/
│
├── calculator/                # All core logic modules
│   ├── __init__.py
│   ├── basic.py
│   ├── scientific.py
│   ├── financial.py
│   ├── planning.py
│   ├── graphical.py
│
├── api/                       # All API endpoints (one per module or grouped)
│   ├── __init__.py
│   ├── basic_api.py
│   ├── scientific_api.py
│   ├── financial_api.py
│   ├── planning_api.py
│   ├── graphical_api.py
│   ├── graphical_advanced_api.py
│
├── tests/                     # All test cases
│   ├── __init__.py
│   ├── test_basic.py
│   ├── test_scientific.py
│   ├── test_financial.py
│   ├── test_planning.py
│   ├── test_graphical.py
│
├── frontend/                  # (Optional) Frontend files
│   ├── index.html
│   ├── style.css
│   ├── main.js
│
├── run_tests_to_csv_simple.py # Test runner/exporter
├── calculator.py              # Main CLI entry point (user menu)
├── INSTRUCTIONS.md            # Usage and architecture guide
├── README.md                  # Project overview
└── requirements.txt           # Dependencies
```

---

For full details, see [INSTRUCTIONS.md](INSTRUCTIONS.md) and the code in each module.

Feel free to extend with more features, a GUI frontend, or additional API endpoints!
