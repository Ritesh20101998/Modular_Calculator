from flask import Flask, request, jsonify, send_file
import io
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/calculate/graphical/plot', methods=['POST'])
def plot_formula():
    data = request.json
    formula = data.get('formula')  # e.g., "np.sin(x) + x**2"
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
        return send_file(buf, mimetype='image/png', as_attachment=False, download_name='plot.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
