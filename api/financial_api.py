from flask import Flask, request, jsonify
from calculator import financial

app = Flask(__name__)

@app.route('/calculate/finance', methods=['POST'])
def calculate_finance():
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

if __name__ == '__main__':
    app.run(debug=True)
