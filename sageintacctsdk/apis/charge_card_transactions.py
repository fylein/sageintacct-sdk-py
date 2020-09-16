"""
Sage Intacct charge card transactions
"""
from typing import Dict

from .api_base import ApiBase


class ChargeCardTransactions(ApiBase):
    """Class for Charge Card Transactions APIs."""

    def post(self, data: Dict):
        """Post charge card transactions to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'record_cctransaction': data
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get charge card transactions from Sage Intacct

        Parameters:
            field (str): A parameter to filter charge card transactions by the field. (required).
            value (str): A parameter to filter charge card transactions by the field - value. (required).

        Returns:
            Dict in charge card transactions schema.
        """
        data = {
            'readByQuery': {
                'object': 'CCTRANSACTION',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

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
