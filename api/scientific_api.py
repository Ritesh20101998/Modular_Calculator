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
        result = math.log(x)
    elif op == 'exp':
        result = math.exp(x)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
