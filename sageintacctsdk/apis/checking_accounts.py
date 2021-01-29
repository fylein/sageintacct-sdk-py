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
        data = {
            'readByQuery': {
                'object': 'CHECKINGACCOUNT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']
