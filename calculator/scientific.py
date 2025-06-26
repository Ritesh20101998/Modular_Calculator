import logging
logging.basicConfig(
    filename='scientific.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
import math

def power(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both arguments must be numbers.")
    try:
        result = math.pow(x, y)
        if result == float('inf') or result == float('-inf'):
            return float('inf')
        return result
    except Exception as e:
        logging.exception(f"power | x={x}, y={y} | error={e}")
        raise

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    if x < 0:
        raise ValueError("Cannot take sqrt of negative number.")
    try:
        result = math.sqrt(x)
        logging.info(f"sqrt | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"sqrt | x={x} | error={e}")
        raise

def log(x, base=None):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    try:
        if base is not None:
            result = math.log(x, base)
        else:
            result = math.log(x)
        logging.info(f"log | x={x}, base={base} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"log | x={x}, base={base} | error={e}")
        raise

def exp(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    try:
        result = math.exp(x)
        logging.info(f"exp | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"exp | x={x} | error={e}")
        raise

def sine(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    try:
        result = math.sin(math.radians(x))
        logging.info(f"sine | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"sine | x={x} | error={e}")
        raise

def cosine(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    try:
        result = math.cos(math.radians(x))
        logging.info(f"cosine | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"cosine | x={x} | error={e}")
        raise

def tangent(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    try:
        result = math.tan(math.radians(x))
        logging.info(f"tangent | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"tangent | x={x} | error={e}")
        raise
