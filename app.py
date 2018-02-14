from flask import Flask, jsonify, render_template
from bank_aggregators import *
from constants import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    op = OPAggregator('OP', OP_HEADERS, OP_BASE_URL)
    nordea = NordeaAggregator('Nordea', NORDEA_HEADERS, NORDEA_BASE_URL)
    op_response = op.get_all_accounts()
    op_total_balance = 0
    for account in op_response:
        op_total_balance += account['balance']

    nordea_raw_resp = nordea.get_all_accounts()
    nordea_account_dump = nordea_raw_resp.get('response', None)

    nord_total_balance = 0
    if not nordea_account_dump:
        return jsonify({'Error': 'Fuck me '})
    nord_accounts = nordea_account_dump.get('accounts', None)
    if not nord_accounts:
        return jsonify({'Error': 'Fuck you '})
    for n_account in nord_accounts:
        nord_total_balance += float(n_account['availableBalance'])

    return jsonify({
        'op': op_total_balance,
        'nordea': nord_total_balance,
        'total_balaance': round((op_total_balance + nord_total_balance), 2)

    })

    nordea_accounts = nord.get_all_accounts()
    return jsonify({op.name: op_response, nord.name: nordea_accounts})


@app.route('/op', methods=['GET'])
def op_accounts():
    op = OPAggregator('OP', OP_HEADERS, OP_BASE_URL)
    op_response = op.get_all_accounts()
    return jsonify({'op': op_response})


@app.route('/nordea', methods=['GET'])
def nordea_accounts():
    nordea = NordeaAggregator('Nordea', NORDEA_HEADERS, NORDEA_BASE_URL)
    nordea = nordea.get_all_accounts()
    return jsonify({'nordea': nordea.pop('response')})



if __name__ == '__main__':
    app.run(port=8000)
