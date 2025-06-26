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
    result = x * y
    if result == float('inf') or result == float('-inf'):
        return float('inf')
    return result

@log_and_handle
def divide(x, y):
    """Return the quotient of x and y, or an error message if y is zero."""
    if y == 0:
        logging.warning(f"divide | x={x}, y={y} | error=Division by zero")
        return "Error: Division by zero!"
    return x / y

@log_and_handle
def modulus(x, y):
    """Return the modulus of x and y, or an error message if y is zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        logging.warning(f"modulus | x={x}, y={y} | error=Division by zero")
        return "Error: Division by zero!"
    return x % y

@log_and_handle
def floor_divide(x, y):
    """Return the floor division of x and y, or an error message if y is zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    if y == 0:
        logging.warning(f"floor_divide | x={x}, y={y} | error=Division by zero")
        return "Error: Division by zero!"
    return x // y

@log_and_handle
def power(x, y):
    """Return x raised to the power y."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")
    try:
        result = x ** y
        if result == float('inf') or result == float('-inf'):
            return float('inf')
        return result
    except OverflowError:
        return float('inf')

@log_and_handle
def max_value(x, y):
    """Return the maximum of x and y."""
    return max(x, y)

@log_and_handle
def min_value(x, y):
    """Return the minimum of x and y."""
    return min(x, y)

@log_and_handle
def abs_value(x):
    """Return the absolute value of x."""
    return abs(x)

# Aliases for compatibility with tests and API
max = max_value
min = min_value
abs = abs_value
