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
    return x + y

@log_and_handle
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

@log_and_handle
def multiply(x, y):
    """Return the product of x and y."""
    return x * y

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
    if y == 0:
        logging.warning(f"modulus | x={x}, y={y} | error=Division by zero")
        return "Error: Division by zero!"
    return x % y

@log_and_handle
def floor_divide(x, y):
    """Return the floor division of x and y, or an error message if y is zero."""
    if y == 0:
        logging.warning(f"floor_divide | x={x}, y={y} | error=Division by zero")
        return "Error: Division by zero!"
    return x // y

@log_and_handle
def power(x, y):
    """Return x raised to the power y."""
    return x ** y

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
