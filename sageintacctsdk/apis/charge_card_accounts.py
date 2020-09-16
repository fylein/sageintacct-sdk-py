"""
Sage Intacct charge card accounts
"""
from typing import Dict

from .api_base import ApiBase


class ChargeCardAccounts(ApiBase):
    """Class for Charge Card Accounts APIs."""

    def get(self, id: str):
        """Get charge card account from Sage Intacct

        Parameters:
            id (str): A parameter to get charge card account by the CARDID. (required).

        Returns:
            Dict in Charge Card Account schema.
        """
        data = {
            'readByName': {
                'object': 'CREDITCARD',
                'keys': id,
                'fields': '*'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all charge card accounts from Sage Intacct

        Returns:
            List of Dict in Charge Card Account schema.
        """
        data = {
            'readByQuery': {
                'object': 'CREDITCARD',
                'fields': '*',
                'query': "LIABILITYTYPE = 'Credit'",
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['creditcard']
