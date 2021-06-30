"""
Sage Intacct AR Invoice
"""
from typing import Dict

from .api_base import ApiBase


class ARInvoice(ApiBase):
    """Class for AR Invoice APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARINVOICE')

    def get_all(self):
        """Get all AR Invoices from Sage Intacct

        Returns:
            List of Dict in AR Invoice schema.
        """
        data = {
            'readByQuery': {
                'object': 'ARINVOICE',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['arinvoice']
