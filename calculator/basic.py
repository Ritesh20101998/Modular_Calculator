"""
Basic Calculator Module
- add, subtract, multiply, divide, modulus, floor_divide
- All functions type-checked and logged
"""

import logging
from functools import wraps

logging.basicConfig(
    filename='basic.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_and_handle(func):
    """Decorator to log function calls and handle exceptions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} | args={args}, kwargs={kwargs} | result={result}")
            return result
        except Exception as e:
            logging.exception(f"{func.__name__} | args={args}, kwargs={kwargs} | error={e}")
            raise
    return wrapper

@log_and_handle
def add(x, y):
    """Return the sum of x and y."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    return x + y

@log_and_handle
def subtract(x, y):
    """Return the difference of x and y."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    return x - y

@log_and_handle
def multiply(x, y):
    """Return the product of x and y."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    return x * y

@log_and_handle
def divide(x, y):
    """Return the division of x by y, or error if y is zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        return "Error: Division by zero!"
    return x / y

@log_and_handle
def modulus(x, y):
    """Return the modulus of x by y, or error if y is zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        return "Error: Division by zero!"
    return x % y

@log_and_handle
def floor_divide(x, y):
    """Return the floor division of x by y, or error if y is zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        return "Error: Division by zero!"
    return x // y
