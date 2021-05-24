"""
Sage Intacct AP Payments
"""
from typing import Dict

from .api_base import ApiBase


class APPayments(ApiBase):
    """Class for AP Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APPYMT')

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
