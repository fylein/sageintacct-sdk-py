"""
Sage Intacct charge card transactions
"""
from typing import Dict

from .api_base import ApiBase


class ChargeCardTransactions(ApiBase):
    """Class for Charge Card Transactions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CCTRANSACTION', post_legacy_method='record_cctransaction')

    def get_all(self):
        """Get all charge card transactions from Sage Intacct

        Returns:
            List of Dict in Charge Card Transactions schema.
        """
        data = {
            'readByQuery': {
                'object': 'CCTRANSACTION',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['cctransaction']

    def update_attachment(self, key: str, supdocid: str):
        """Update charge card transactions with supdocid

        Parameters:
            key (str): A parameter to update charge card transactions by the key. (required).
            supdoc (str): A parameter to update attachment ID for the charge card transactions. (required).

        Returns:
            Dict in Charge Card Transactions update schema.
        """
        data = {
            'update_cctransaction': {
                '@key': key,
                'supdocid': supdocid
            }
        }

        return self.format_and_send_request(data)
