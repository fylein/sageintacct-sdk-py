"""
Sage Intacct AP Payments
"""
from typing import Dict

from .api_base import ApiBase


class APPayments(ApiBase):
    """Class for AP Payments APIs."""

    def post(self, data: Dict):
        """Post AP Payments to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'APPYMT': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get AP Payment from Sage Intacct

        Parameters:
            field (str): A parameter to filter AP Payments by the field. (required).
            value (str): A parameter to filter AP Payments by the field - value. (required).

        Returns:
            Dict in AP Payments schema.
        """
        data = {
            'readByQuery': {
                'object': 'APPYMT',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['appymt']

    def get_all(self):
        """Get all AP Payments from Sage Intacct

        Returns:
            List of Dict in AP Payments schema.
        """
        data = {
            'readByQuery': {
                'object': 'APPYMT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['appymt']
