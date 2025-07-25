"""
Graphical Calculator Module
- Plotting and visualization utilities
- Uses numpy and matplotlib, logs all actions
"""

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
    """Plot the function y = x^2 and return the image as BytesIO."""
    import io
    try:
        x = np.linspace(-10, 10, 400)
        y = x ** 2
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('y = x^2')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        logging.info("plot_y_equals_x_squared | success")
        return buf
    except Exception as e:
        logging.exception(f"plot_y_equals_x_squared | error={e}")
        raise

def plot_multiple_functions(functions, labels=None, x_range=(-10, 10), num_points=400, title='Multiple Functions'):
    """
    Plot multiple mathematical functions on the same graph.
    Args:
        functions: List of callables, each taking a numpy array and returning y values.
        labels: List of labels for each function (optional).
        x_range: Tuple (min, max) for x-axis.
        num_points: Number of points to plot.
        title: Title of the plot.
    """
    try:
        x = np.linspace(x_range[0], x_range[1], num_points)
        plt.figure()
        for i, func in enumerate(functions):
            y = func(x)
            label = labels[i] if labels and i < len(labels) else f'Function {i+1}'
            plt.plot(x, y, label=label)
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        if labels:
            plt.legend()
        plt.show()
        logging.info(f"plot_multiple_functions | success | functions={len(functions)}")
    except Exception as e:
        logging.exception(f"plot_multiple_functions | error={e}")
        print(f"Error: {e}")
