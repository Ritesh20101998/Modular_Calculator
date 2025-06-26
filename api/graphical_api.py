from flask import Flask, request, jsonify, send_file
import io
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/calculate/graphical', methods=['POST'])
def calculate_graphical():
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
    app.run(debug=True)
