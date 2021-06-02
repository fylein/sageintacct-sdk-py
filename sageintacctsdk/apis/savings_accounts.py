"""
Sage Intacct Savings Accounts
"""
from .api_base import ApiBase


class SavingsAccounts(ApiBase):
    """Class for Savings Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SAVINGSACCOUNT')

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
