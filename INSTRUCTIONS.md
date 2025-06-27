# Modular Calculator: Instructions & Feature Guide

This document explains how the Modular Calculator project works, its architecture, and details all available functions and features.

---

## Overview

The Modular Calculator is a Python-based, extensible calculator system with a modular architecture. It supports basic, scientific, financial, and graphical calculations, each in its own module. The project exposes a REST API for programmatic access and (optionally) a frontend for user interaction.

---

## Project Structure

- `calculator/`
  - `basic.py` — Basic arithmetic operations
  - `scientific.py` — Scientific functions
  - `financial.py` — Financial calculations
  - `graphical.py` — Graph plotting utilities
- `api/`
  - `basic_api.py` — API for basic operations
  - `calculator_api.py` — (optional, can be removed) Unified API
- `tests/` — Unit tests for all modules
- `frontend/` — (optional) HTML/JS frontend

---

## How It Works

Each calculator module defines a set of functions. The API modules expose these functions via HTTP POST endpoints. You can use the API by sending JSON requests to the endpoints, or import the modules directly in Python code.

---

## Module & Function Details

### 1. Basic Calculator (`calculator/basic.py`)

**Functions:**
- `add(x, y)` — Returns the sum of `x` and `y`.
- `subtract(x, y)` — Returns the difference (`x - y`).
- `multiply(x, y)` — Returns the product.
- `divide(x, y)` — Returns the quotient (`x / y`). Handles division by zero.
- `modulus(x, y)` — Returns `x % y`.
- `floor_divide(x, y)` — Returns `x // y`.
- `power(x, y)` — Returns `x ** y`.
- `max(x, y)` — Returns the maximum of `x` and `y`.
- `min(x, y)` — Returns the minimum of `x` and `y`.
- `abs(x)` — Returns the absolute value of `x`.

### 2. Scientific Calculator (`calculator/scientific.py`)

**Functions:**
- `power(x, y)` — Exponentiation.
- `sqrt(x)` — Square root.
- `sine(x)` — Sine of `x` (in radians).
- `cosine(x)` — Cosine of `x` (in radians).
- `tangent(x)` — Tangent of `x` (in radians).
- `log(x, base=None)` — Logarithm of `x` (natural log if `base` is not provided).
- `exp(x)` — Exponential (`e ** x`).

### 3. Financial Calculator (`calculator/financial.py`)

**Functions:**
- `simple_interest(p, r, t)` — Simple interest: `p * r * t / 100`.
- `compound_interest(p, r, t, n)` — Compound interest: `p * (1 + r/(100*n))**(n*t) - p`.
- (Other financial functions may be present, e.g., risk analysis, currency formatting.)

### 4. Graphical Calculator (`calculator/graphical.py`)

**Functions:**
- `plot_y_equals_x_squared()` — Plots `y = x^2` and returns a PNG image buffer.
- (Advanced plotting: may support custom formulas via API.)

---

## API Endpoints

- `/calculate/basic` — Basic operations (see above)
- `/calculate/scientific` — Scientific operations
- `/calculate/finance` — Financial operations
- `/calculate/graphical` — Graphical operations (returns image)

**Usage:**
- Send a POST request with JSON body specifying the operation and parameters.

### Example Requests

#### Basic Calculator
```json
{
  "operation": "add",
  "x": 2,
  "y": 3
}
```
Response:
```json
{
  "result": 5
}
```

#### Scientific Calculator
```json
{
  "operation": "sqrt",
  "x": 16
}
```
Response:
```json
{
  "result": 4.0
}
```

#### Financial Calculator
```json
{
  "operation": "simple_interest",
  "p": 1000,
  "r": 5,
  "t": 2
}
```
Response:
```json
{
  "result": 100.0
}
```

#### Graphical Calculator
```json
{
  "operation": "plot_y_equals_x_squared"
}
```
Response: PNG image (as file/binary)

---

## Error Handling
- All functions check for invalid input and return clear error messages.
- Division by zero and domain errors are handled gracefully.

---

## Extending the Calculator
- Add new functions to the relevant module (e.g., `scientific.py`).
- Add a corresponding API endpoint or extend an existing one.
- Add tests in the `tests/` directory.

---

## Running & Testing
- Start the API: `python api/basic_api.py`
- Run tests: `python -m unittest discover tests`

---

## Frontend (Optional)
- The `frontend/` directory contains a simple HTML/JS interface for user interaction.
- You can serve it with any static file server or integrate it with Flask if needed.

---

For more details, see the code in each module and the README.
