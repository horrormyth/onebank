from requests import request
from constants import OP, NORDEA, NORDEA_HEADERS, OP_HEADERS, OP_BASE_URL, NORDEA_BASE_URL


class BankAggrigatorError(Exception):
    pass


class BankAggrigator(object):
    def __init__(self, name):
        self.name = name
        if self.name in [OP,NORDEA]:
            if self.name == NORDEA:
                self.header = NORDEA_HEADERS
                self.base_url = NORDEA_BASE_URL
            else:
                self.header = OP_HEADERS
                self.base_url = OP_HEADERS
        else:
            raise BankAggrigatorError('Provided bank not found')

    def _request(self, method, url, data=None):
        """Custom request to handle all the requests types one point solution """
        response = request(method=method, url=url, headers=self.header)
        if not response.ok:
            return None
        return response

    def get_all_accounts(self):
        """

        :return:
        :rtype:get
        """
        pass

    def get_account(self, account_id):
        """

        :param account_id:
        :type account_id:
        :return:
        :rtype: get
        """
        pass

    def get_all_transaction_of_an_account(self, account_id):
        """

        :param account_id:
        :type account_id:
        :return:
        :rtype: get
        """
        pass

    def get_transaction_detail(self, account_id, transaction_id):
        """

        :param account_id:
        :type account_id:
        :param transaction_id:
        :type transaction_id:
        :return:
        :rtype: get
        """

    def initiate_payment(self, sender_iban, receiver_iban, amount=0):
        """

        :param sender_iban:
        :type sender_iban:
        :param receiver_iban:
        :type receiver_iban:
        :param amount:
        :type amount:
        :return:
        :rtype: get
        """
        pass
