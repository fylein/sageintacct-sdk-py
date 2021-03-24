"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Accounts APIs."""

    def post(self, data: Dict):
        """Post general ledger account to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'GLACCOUNT': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get general ledger account from Sage Intacct

        Parameters:
            field (str): A parameter to filter general ledger account by the field. (required).
            value (str): A parameter to filter general ledger account by the field - value. (required).

        Returns:
            Dict in Location schema.
        """
        data = {
            'readByQuery': {
                'object': 'GLACCOUNT',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all general ledger accounts from Sage Intacct

        Returns:
            List of Dict in General Ledger Account schema.
        """
        total_gl_accounts = []
        get_count = {
            'query': {
                'object': 'GLACCOUNT',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 1000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'GLACCOUNT',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'ACCOUNTNO',
                            'TITLE',
                            'ACCOUNTTYPE',
                            'NORMALBALANCE',
                            'CLOSINGTYPE',
                            'STATUS',
                            'CATEGORY',
                            'ALTERNATIVEACCOUNT'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            gl_accounts = self.format_and_send_request(data)['data']['GLACCOUNT']
            total_gl_accounts = total_gl_accounts + gl_accounts
            offset = offset + pagesize

        return total_gl_accounts
