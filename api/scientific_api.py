from flask import Flask, request, jsonify
from calculator import scientific
import math

app = Flask(__name__)

@app.route('/calculate/scientific', methods=['POST'])
def calculate_scientific():
    data = request.json
    op = data.get('operation')
    x = data.get('x')
    y = data.get('y')
    base = data.get('base')
    if op is None:
        return jsonify({'error': 'Missing operation.'}), 400
    if op in ['power']:
        if x is None or y is None or not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return jsonify({'error': 'x and y must be numbers.'}), 400
    elif op in ['sqrt', 'sine', 'cosine', 'tangent', 'log', 'exp']:
        if x is None or not isinstance(x, (int, float)):
            return jsonify({'error': 'x must be a number.'}), 400
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
    elif op == 'log':
        if base is not None:
            if not isinstance(base, (int, float)):
                return jsonify({'error': 'base must be a number.'}), 400
            result = math.log(x, base)
        else:
            result = math.log(x)
    elif op == 'exp':
        result = math.exp(x)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
