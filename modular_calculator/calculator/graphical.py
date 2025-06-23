# ...existing code from your graphical.py...

import logging
logging.basicConfig(
    filename='graphical.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
try:
    import matplotlib.pyplot as plt
except ImportError:
    msg = ("matplotlib is required for graphical calculator.\n"
           "To install, run: pip install matplotlib")
    print(msg)
    raise

try:
    import numpy as np
except ImportError:
    msg = ("numpy is required for graphical calculator.\n"
           "To install, run: pip install numpy")
    print(msg)
    raise

def plot_y_equals_x_squared():
    """Plot the function y = x^2 and display the graph."""
    try:
        x = np.linspace(-10, 10, 400)
        y = x ** 2
        plt.plot(x, y)
        plt.title('y = x^2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
        logging.info("plot_y_equals_x_squared | success")
    except Exception as e:
        logging.exception(f"plot_y_equals_x_squared | error={e}")
        print(f"Error: {e}")
