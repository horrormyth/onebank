from flask import Flask
from bank_aggregators import OPAggregator, NordeaAggregator
from constants import OP_HEADERS, OP_BASE_URL, NORDEA_HEADERS, NORDEA_BASE_URL
import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    OP_HEADERS['x-api-key']='3Ur2dtArrTNQuIluR9XBWOfeQW5A8MoR'
    op = OPAggregator('OP', OP_HEADERS, OP_BASE_URL)
    nordea = NordeaAggregator('Nordea', NORDEA_HEADERS, NORDEA_BASE_URL)
    op_data = op.get_all_accounts()
    nord_data = nordea.get_all_accounts()
    print op_data

    return jsonify({op.name: op_data})


@app.route('/accounts', methods=['GET'])
def accounts():
    op = OPAggregator('OP', OP_HEADERS, OP_BASE_URL)
    op_accounts = op.get_all_accounts()
    print(op_accounts)
    return 'tesltlksjl'


if __name__ == '__main__':
    app.run()
