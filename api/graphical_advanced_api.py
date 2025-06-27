from flask import Flask, request, jsonify, send_file
import io
import matplotlib.pyplot as plt
import numpy as np
import logging
import re

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Allow only safe characters in formula (numbers, x, np, math ops, parentheses, dot)
SAFE_FORMULA_RE = re.compile(r'^[\d\s\+\-\*/\(\)xnp\.\,\*\*]+$')

@app.route('/calculate/graphical/plot', methods=['POST'])
def plot_formula():
    data = request.json
    formula = data.get('formula')  # e.g., "np.sin(x) + x**2"
    logging.info(f"Received formula: {formula}")
    if not formula or not isinstance(formula, str):
        logging.warning("Formula missing or not a string.")
        return jsonify({'error': 'Formula must be a non-empty string.'}), 400
    if not SAFE_FORMULA_RE.match(formula.replace('np.sin', '').replace('np.cos', '').replace('np.tan', '').replace('np.exp', '').replace('np.log', '')):
        logging.warning("Formula contains unsafe characters or functions.")
        return jsonify({'error': 'Formula contains unsafe characters or functions.'}), 400
    x = np.linspace(-10, 10, 400)
    try:
        # Only allow numpy and x in eval for safety
        y = eval(formula, {"np": np, "x": x})
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f'y = {formula}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        logging.info("Plot generated successfully.")
        return send_file(buf, mimetype='image/png', as_attachment=False, download_name='plot.png')
    except Exception as e:
        logging.error(f"Error evaluating formula: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
