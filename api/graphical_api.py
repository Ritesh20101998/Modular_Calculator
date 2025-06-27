from flask import Flask, request, jsonify, send_file
import io
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/calculate/graphical', methods=['POST'])
def calculate_graphical():
    data = request.json
    op = data.get('operation')
    if not op or not isinstance(op, str):
        return jsonify({'error': 'Missing or invalid operation.'}), 400
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

@app.route('/test_results/pie_chart', methods=['POST'])
def test_results_pie_chart():
    """
    Expects JSON: {"results": ["pass", "fail", "pass", ...]}
    Returns a PNG pie chart of test case results.
    """
    data = request.json
    results = data.get('results')
    if not results or not isinstance(results, list):
        return jsonify({'error': 'Missing or invalid results list.'}), 400
    # Count occurrences
    from collections import Counter
    counts = Counter(results)
    labels = list(counts.keys())
    sizes = list(counts.values())
    colors = []
    for label in labels:
        if label == 'pass':
            colors.append('#4CAF50')  # green
        elif label == 'fail':
            colors.append('#F44336')  # red
        elif label == 'error':
            colors.append('#FFC107')  # yellow
        else:
            colors.append('#9E9E9E')  # grey
    plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Test Case Results Distribution')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=False, download_name='test_results_pie.png')

if __name__ == '__main__':
    app.run(debug=True)
