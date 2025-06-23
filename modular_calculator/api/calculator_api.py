from flask import Flask, request, jsonify, send_file
import io
import matplotlib.pyplot as plt
import numpy as np
from calculator import basic, scientific, financial

# Initialize Flask app
app = Flask(__name__)

@app.route('/calculate/basic', methods=['POST'])
def calculate_basic():
    """
    Handle basic arithmetic operations via POST request.
    Expects JSON with 'operation', 'x', and 'y' (or just 'x' for abs).
    Supported operations: add, subtract, multiply, divide, modulus, floor_divide, power, max, min, abs.
    Returns result as JSON or error if invalid operation.
    """
    data = request.json
    op = data.get('operation')
    x = data.get('x')
    y = data.get('y')
    # Basic operations
    if op == 'add':
        result = basic.add(x, y)
    elif op == 'subtract':
        result = basic.subtract(x, y)
    elif op == 'multiply':
        result = basic.multiply(x, y)
    elif op == 'divide':
        result = basic.divide(x, y)
    elif op == 'modulus':
        result = basic.modulus(x, y)
    elif op == 'floor_divide':
        result = basic.floor_divide(x, y)
    elif op == 'power':
        result = basic.power(x, y)
    # Advanced features
    elif op == 'max':
        result = max(x, y)
    elif op == 'min':
        result = min(x, y)
    elif op == 'abs':
        result = abs(x)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

@app.route('/calculate/scientific', methods=['POST'])
def calculate_scientific():
    """
    Handle scientific operations via POST request.
    Expects JSON with 'operation', 'x', and optionally 'y'.
    Supported operations: power, sqrt, sine, cosine, tangent, log, exp.
    Returns result as JSON or error if invalid operation.
    """
    data = request.json
    op = data.get('operation')
    x = data.get('x')
    y = data.get('y')
    if op == 'power':
        result = scientific.power(x, y)
    elif op == 'sqrt':
        result = scientific.sqrt(x)
    elif op == 'sine':
        result = scientific.sine(x)
    elif op == 'cosine':
        result = scientific.cosine(x)
    elif op == 'tangent':
        result = scientific.tangent(x)
    # Advanced features
    elif op == 'log':
        import math
        result = math.log(x)
    elif op == 'exp':
        import math
        result = math.exp(x)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

@app.route('/calculate/finance', methods=['POST'])
def calculate_finance():
    """
    Handle financial calculations via POST request.
    Expects JSON with 'operation' and required parameters (p, r, t, n).
    Supported operations: simple_interest, compound_interest.
    Returns result as JSON or error if invalid operation.
    """
    data = request.json
    op = data.get('operation')
    if op == 'simple_interest':
        p = data.get('p')
        r = data.get('r')
        t = data.get('t')
        result = financial.simple_interest(p, r, t)
    elif op == 'compound_interest':
        p = data.get('p')
        r = data.get('r')
        t = data.get('t')
        n = data.get('n')
        result = financial.compound_interest(p, r, t, n)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

@app.route('/calculate/graphical', methods=['POST'])
def calculate_graphical():
    """
    Handle graphical operations via POST request.
    Expects JSON with 'operation'.
    Supported operations: plot_y_equals_x_squared (returns PNG image of plot).
    Returns image or error if invalid operation.
    """
    data = request.json
    op = data.get('operation')
    if op == 'plot_y_equals_x_squared':
        try:
            x = np.linspace(-10, 10, 400)
            y = x ** 2
            plt.figure()
            plt.plot(x, y)
            plt.title('y = x^2')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return send_file(buf, mimetype='image/png', as_attachment=False, download_name='plot.png')
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid operation'}), 400

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
