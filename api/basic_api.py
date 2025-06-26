from flask import Flask, request, jsonify
from calculator import basic

app = Flask(__name__)

@app.route('/calculate/basic', methods=['POST'])
def calculate_basic():
    data = request.json
    op = data.get('operation')
    x = data.get('x')
    y = data.get('y')
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
    elif op == 'max':
        result = max(x, y)
    elif op == 'min':
        result = min(x, y)
    elif op == 'abs':
        result = abs(x)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
