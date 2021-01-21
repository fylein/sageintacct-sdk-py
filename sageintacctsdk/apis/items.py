"""
Sage Intacct items
"""
from typing import Dict

from .api_base import ApiBase


class Items(ApiBase):
    """Class for Items APIs."""

    def post(self, data: Dict):
        """Post item to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'ITEM': data
            }
        }
        return self.format_and_send_request(data)

    def get_all(self):
        """Get all items from Sage Intacct

        Returns:
            List of Dict in Items schema.
        """
        data = {
            'readByQuery': {
                'object': 'ITEM',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['item']
