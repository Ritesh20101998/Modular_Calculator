# Python Modular Calculator

A robust, modular calculator project in Python supporting Basic, Scientific, Financial, and Graphical calculations. Includes a REST API, logging, error handling, and unit tests.

## Features
- **Basic Calculator:** Addition, subtraction, multiplication, division, modulus, floor division, power, max, min, abs.
- **Scientific Calculator:** Power, square root, sine, cosine, tangent, log, exp, advanced error handling.
- **Financial Calculator:** Simple/compound interest, risk & return analysis, currency formatting, CSV/Excel/SQLite support, robust error handling.
- **Graphical Calculator:** Plots (e.g., y = x²) as PNG images via API, extensible for more plots.
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

## API Endpoints
- `/calculate/basic` — Basic operations (add, subtract, multiply, divide, modulus, floor_divide, power, max, min, abs)
- `/calculate/scientific` — Scientific operations (power, sqrt, sine, cosine, tangent, log, exp)
- `/calculate/finance` — Financial operations (simple_interest, compound_interest, risk_return_analysis, format_currency, data import/export)
- `/calculate/graphical` — Graphical operations (e.g., plot_y_equals_x_squared)

All endpoints accept POST requests with JSON payloads. See code and tests for details.

## Project Structure
- `calculator/` — All calculator modules (basic, scientific, financial, graphical)
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

## Extending the Project
- Add new operations by creating new functions in the relevant module and exposing them via the API.
- Add new API endpoints in `api/calculator_api.py`.
- Add new tests in `tests/test_calculator.py`.
- Follow the modular and documented style for maintainability.

## Contributing
Pull requests are welcome! Please add tests for new features and update documentation as needed.

## License
MIT License

---
Feel free to extend with more features, a GUI frontend, or additional API endpoints!
