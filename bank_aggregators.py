import json
from datetime import datetime

from requests import request

from constants import GET, POST, PUT
from generate_access_token import generate_access_token


# Add this to nordea
# self.header['Authorization']= 'Bearer {}'.format(generate_access_token),

class BaseBankAggregator(object):
    def __init__(self, name, headers, base_url):
        self.name = name
        self.headers = headers
        self.base_url = base_url

    def _request(self, method, url, data=None):
        """Custom request tquests types one point solution """
        response = request(method=method, url=url, headers=self.headers, json=data)
        if not response.ok:
            return None
        return response.json()


class OPAggregator(BaseBankAggregator):
    def get_all_accounts(self):
        """

        :return:
        :rtype:get
        """
        url = '{}/v1/accounts'.format(self.base_url)
        response = self._request(GET, url)
        return response

    def get_account_by_id(self, account_id):
        """

        :param account_id:
        :type account_id:
        :return:
        :rtype: get
        """
        url = '{}/v1/accounts/{}'.format(self.base_url, account_id)
        response = self._request(GET, url)
        return response

    def get_all_transaction_of_an_account(self, account_id):
        """

        :param account_id:
        :type account_id:
        :return:
        :rtype: get
        """
        url = '{}/v1/accounts/{}/transactions'.format(self.base_url, account_id)
        response = self._request(GET, url)
        return response

    def get_transaction_detail(self, account_id, transaction_id):
        """

        :param account_id:
        :type account_id:
        :param transaction_id:
        :type transaction_id:
        :return:
        :rtype: get
        """
        url = '{}/v1/accounts/{}/transactions/{}'.format(self.base_url, account_id, transaction_id)
        response = self._request(GET, url)
        return response

    def initiate_payment(self,
                         sender_iban,
                         receiver_iban,
                         amount=0,
                         subject='Test',
                         currency='EUR',
                         receiver_bic=None,
                         receiver_name=None,
                         ):
        """

        :param sender_iban:
        :param receiver_iban:
        :param amount: int
        :param subject: string
        :param currency: 'EUR/USD etc
        :param receiver_bic: string
        :param receiver_name:  string
        :return: json response
        """
        payload = {
            "amount": amount,
            "subject": subject,
            "currency": currency,
            "payerIban": sender_iban,
            "valueDate": datetime.utcnow().isoformat(),
            "receiverBic": "string",
            "receiverIban": receiver_iban,
            "receiverName": "string"
        }

        url = '{}/v1/payments/initiate'.format(self.base_url)
        response = self._request(POST, url, data=payload)
        return response

    def confirm_payment(self, payment_id):
        """
        Confirms initiated payment
        :param payment_id:
        :return:
        """
        payload = {
            'paymentId': payment_id
        }
        url = '{}/v1/payments/confirm'.format(self.base_url)
        response = self._request(POST, url, data=payload)
        return response


class NordeaAggregator(BaseBankAggregator):
    def __init__(self, name, headers, base_url):
        super(NordeaAggregator, self).__init__(name, headers, base_url)
        self.headers['Authorization'] = 'Bearer {}'.format(generate_access_token())

    def get_all_accounts(self):
        url = '{}v2/accounts'.format(self.base_url)
        response = self._request(GET, url)
        return response

    def get_account_by_id(self, account_id):
        url = '{}v2/accounts/{}'.format(self.base_url, account_id)
        response = self._request(GET, url)
        return response

    def get_all_transactions_of_an_account(self, account_id):
        url = 'v2/accounts/{}/transactions'
        response = self._request(GET, url)
        return response

    def get_all_payments(self):
        url = 'v2/payments/sepa'
        response = self._request(GET, url)
        return response

    def get_payment_by_id(self, payment_id):
        url = 'v2/payments/sepa/{}'.format(payment_id)
        response = self._request(GET, url)
        return response

    def initiate_payment(self,

                         creditor_account_type,
                         creditor_account,
                         debtor_account,
                         message='default',
                         amount=0,
                         currency='EUR',
                         creditor_name='',
                         ):
        payload = {
            "amount": amount,
            "creditor": {
                "account": {
                    "_type": creditor_account_type,
                    "value": creditor_account
                },
                "message": message,
                "name": creditor_name,
            },
            "currency": currency,
            "debtor": {
                "_accountId": debtor_account
            }
        }

        url = '{}v2/payments/sepa'.format(self.base_url)
        response = self._request(POST, url, data=json.dumps(payload))
        return response

    def confirm_payment(self, payment_id):
        url = '{}v2/payments/sepa/{}/confirm'.format(self.base_url, payment_id)
        response = self._request(PUT, url)
        return response
