from flask import Flask, request, jsonify
from calculator import financial

app = Flask(__name__)

@app.route('/calculate/finance', methods=['POST'])
def calculate_finance():
    data = request.json
    op = data.get('operation')
    if op is None:
        return jsonify({'error': 'Missing operation.'}), 400
    if op == 'simple_interest':
        p = data.get('p')
        r = data.get('r')
        t = data.get('t')
        if p is None or r is None or t is None or not all(isinstance(val, (int, float)) for val in [p, r, t]):
            return jsonify({'error': 'p, r, t must be numbers.'}), 400
        result = financial.simple_interest(p, r, t)
    elif op == 'compound_interest':
        p = data.get('p')
        r = data.get('r')
        t = data.get('t')
        n = data.get('n')
        if p is None or r is None or t is None or n is None or not all(isinstance(val, (int, float)) for val in [p, r, t, n]):
            return jsonify({'error': 'p, r, t, n must be numbers.'}), 400
        result = financial.compound_interest(p, r, t, n)
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
