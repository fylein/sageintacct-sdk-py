"""
Sage Intacct Savings Accounts
"""
from .api_base import ApiBase


class SavingsAccounts(ApiBase):
    """Class for Savings Accounts APIs."""

    def get(self, card_id: str):
        """Get Savings Account from Sage Intacct

        Parameters:
            card_id (str): A parameter to get Savings Account by the CARDID. (required).

        Returns:
            Dict in Savings Account schema.
        """
        data = {
            'readByName': {
                'object': 'SAVINGSACCOUNT',
                'keys': card_id,
                'fields': '*'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all Savings Accounts from Sage Intacct

        Returns:
            List of Dict in Savings Account schema.
        """
        data = {
            'readByQuery': {
                'object': 'SAVINGSACCOUNT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']
