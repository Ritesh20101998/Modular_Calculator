import logging
logging.basicConfig(
    filename='scientific.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
import math

def power(x, y):
    """Return x raised to the power y."""
    try:
        result = math.pow(x, y)
        logging.info(f"power | x={x}, y={y} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"power | x={x}, y={y} | error={e}")
        raise

def sqrt(x):
    """Return the square root of x."""
    try:
        result = math.sqrt(x)
        logging.info(f"sqrt | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"sqrt | x={x} | error={e}")
        raise

def sine(x):
    """Return the sine of x degrees."""
    try:
        result = math.sin(math.radians(x))
        logging.info(f"sine | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"sine | x={x} | error={e}")
        raise

def cosine(x):
    """Return the cosine of x degrees."""
    try:
        result = math.cos(math.radians(x))
        logging.info(f"cosine | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"cosine | x={x} | error={e}")
        raise

def tangent(x):
    """Return the tangent of x degrees."""
    try:
        result = math.tan(math.radians(x))
        logging.info(f"tangent | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"tangent | x={x} | error={e}")
        raise

def log_value(x):
    """Return the natural logarithm of x."""
    try:
        import math
        result = math.log(x)
        logging.info(f"log | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"log | x={x} | error={e}")
        raise

def exp_value(x):
    """Return the exponential of x (e^x)."""
    try:
        import math
        result = math.exp(x)
        logging.info(f"exp | x={x} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"exp | x={x} | error={e}")
        raise
