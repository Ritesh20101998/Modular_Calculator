from flask import Flask, request, jsonify
from calculator.planning import sip_calculator, lumpsum_calculator, fv, pv, pmt, nper, rate
from calculator.finance import compound_interest
import logging
import os

app = Flask(__name__)

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(
    filename='logs/planning_api.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/api/planning/sip', methods=['POST'])
def api_sip():
    data = request.get_json()
    try:
        result = sip_calculator(
            data['monthly_investment'],
            data['annual_rate'],
            data['tenure_months']
        )
        logging.info(f"SIP API | input={data} | result={result}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"SIP API | input={data} | error={e}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/planning/lumpsum', methods=['POST'])
def api_lumpsum():
    data = request.get_json()
    try:
        # Use compound_interest for lumpsum calculation
        principal = data['principal']
        annual_rate = data['annual_rate']
        tenure_years = data['tenure_years']
        # Compound annually (n=1)
        maturity = principal + compound_interest(principal, annual_rate, tenure_years, 1)
        gain = maturity - principal
        result = {
            'Maturity Value': round(maturity, 2),
            'Total Gain': round(gain, 2)
        }
        logging.info(f"Lumpsum API | input={data} | result={result}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Lumpsum API | input={data} | error={e}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/planning/tvm', methods=['POST'])
def api_tvm():
    data = request.get_json()
    try:
        op = data['operation']
        if op == 'fv':
            result = {'FV': fv(data['pv'], data['rate'], data['n'])}
        elif op == 'pv':
            result = {'PV': pv(data['fv'], data['rate'], data['n'])}
        elif op == 'pmt':
            result = {'PMT': pmt(data['pv'], data['rate'], data['n'])}
        elif op == 'nper':
            result = {'N': nper(data['pv'], data['pmt'], data['rate'])}
        elif op == 'rate':
            result = {'Rate': rate(data['pv'], data['pmt'], data['n'])}
        else:
            raise ValueError('Invalid operation')
        logging.info(f"TVM API | input={data} | result={result}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"TVM API | input={data} | error={e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
