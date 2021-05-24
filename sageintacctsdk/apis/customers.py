"""
Sage Intacct customers
"""
from typing import Dict

from .api_base import ApiBase


class Customers(ApiBase):
    """Class for Customers APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CUSTOMER')

    def get_all(self):
        """Get all customers from Sage Intacct

        Returns:
            List of Dict in Customers schema.
        """
        data = {
            'readByQuery': {
                'object': 'CUSTOMER',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['customer']
