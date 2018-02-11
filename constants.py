import os
from generate_access_token import generate_access_token

OP = 'OP'
NORDEA = 'Nordea'

# endpoint we query
endpoint = 'v2/accounts'
# set headers and make the request

NORDEA_BASE_URL = 'https://api.nordeaopenbanking.com/'
NORDEA_CLIENT_ID = os.environ.get('NORDEA_CLIENT_ID', 'a')
NORDEA_CLIENT_SECRET = os.environ.get('NORDEA_SECRET', 'a')

OP_BASE_URL = "https://sandbox.apis.op-palvelut.fi/"
OP_CLIENT_ID = os.environ.get('OP_CLIENT_ID', None)
OP_CLIENT_SECRET = os.environ.get('OP_SECRET', None)
OP_X_API_KEY = os.environ.get('X_API_KEY', 'LHtDgWLxckHhqvx87UnO6mGYxuHVmaYW'),

NORDEA_HEADERS = {
    'X-IBM-Client-Id': NORDEA_CLIENT_ID,
    'X-IBM-Client-Secret': NORDEA_CLIENT_SECRET,
    'content-type': 'application/json'

}
OP_HEADERS = {
    'x-api-key': OP_X_API_KEY,
    'x-request-id': "12345",
    'x-session-id': "12345",
    'x-authorization': "fdb6c7c24bbc3a2c4144c1848825ab7d3a4ccb43",
    'content-type': 'application/json'
}

REDIRECT_URI = 'https://httpbin.org/get'
