"""
Sage Intacct AR Payments
"""
from typing import Dict

from .api_base import ApiBase


class ARPayments(ApiBase):
    """Class for AR Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARPYMT')

    def get_all(self):
        """Get all AR Payments from Sage Intacct

        Returns:
            List of Dict in AR Payments schema.
        """
        data = {
            'readByQuery': {
                'object': 'ARPYMT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['arpymt']
