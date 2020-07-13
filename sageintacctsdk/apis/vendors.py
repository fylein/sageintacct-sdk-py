"""
Sage Intacct vendors
"""
from typing import Dict

from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Vendors APIs."""

    def post(self, data: Dict):
        """Post vendors to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'VENDOR': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get vendors from Sage Intacct

        Parameters:
            field (str): A parameter to filter vendors by the field. (required).
            value (str): A parameter to filter vendors by the field - value. (required).

        Returns:
            Dict in vendors schema.
        """
        data = {
            'readByQuery': {
                'object': 'VENDOR',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all vendors from Sage Intacct

        Returns:
            List of Dict in Vendors schema.
        """
        data = {
            'readByQuery': {
                'object': 'VENDOR',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['vendor']
