"""
Sage Intacct Checking Accounts
"""
from .api_base import ApiBase


class CheckingAccounts(ApiBase):
    """Class for Checking Accounts APIs."""

    def get(self, card_id: str):
        """Get Checking Account from Sage Intacct

        Parameters:
            card_id (str): A parameter to get Checking Account by the CARDID. (required).

        Returns:
            Dict in Checking Account schema.
        """
        data = {
            'readByName': {
                'object': 'CHECKINGACCOUNT',
                'keys': card_id,
                'fields': '*'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all Checking Accounts from Sage Intacct

        Returns:
            List of Dict in Checking Account schema.
        """
        total_checking_accounts = []
        get_count = {
            'query': {
                'object': 'CHECKINGACCOUNT',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'CHECKINGACCOUNT',
                    'select': {
                        'field': [
                            'BANKACCOUNTID',
                            'BANKACCOUNTNO',
                            'GLACCOUNTNO',
                            'BANKNAME',
                            'ROUTINGNO',
                            'BRANCHID',
                            'BANKACCOUNTTYPE',
                            'DEPARTMENTID',
                            'LOCATIONID',
                            'STATUS',
                            'RECORDNO',
                            'ACHBANKID',
                            'COMPANYNAME'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            checking_accounts = self.format_and_send_request(data)['data']['CHECKINGACCOUNT']
            total_checking_accounts = total_checking_accounts + checking_accounts
            offset = offset + pagesize

        return total_checking_accounts
