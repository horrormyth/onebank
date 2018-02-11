#!/usr/bin/env python3
import requests

API_URI = 'https://api.nordeaopenbanking.com/'
CLIENT_ID = 'your client id here'
CLIENT_SECRET = 'your client secret here'
REDIRECT_URI = 'http://httpbin.org/get'

"""
This is an example how to generate the access token from the scratch.
We first call get_code and then get_access_token function.
Access token can be generated by calling generate_access_token
or by running this file i.e. 'python generate_access_token.py'
"""

def get_code():
    endpoint = 'v1/authentication'
    payload = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': ''
    }
    r = requests.get(API_URI + endpoint, params=payload)
    if not r.status_code == requests.codes.ok:
        raise Exception(r.text)
    response = r.json()
    code = response['args']['code']
    return code


def get_access_token(code):
    endpoint = 'v1/authentication/access_token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-IBM-Client-Id': CLIENT_ID,
        'X-IBM-Client-Secret': CLIENT_SECRET
    }

    payload = {
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    r = requests.post(API_URI + endpoint, data=payload, headers=headers)
    if not r.status_code == requests.codes.ok:
        raise Exception(r.text)

    response = r.json()
    access_token = response['access_token']
    return access_token


def generate_access_token():
    code = get_code()
    access_token = get_access_token(code)
    return access_token


if __name__ == '__main__':
    access_token = generate_access_token()
    print(access_token)