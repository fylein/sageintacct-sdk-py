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
        total_items = []
        get_count = {
            'query': {
                'object': 'ITEM',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'ITEM',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'ITEMID',
                            'STATUS',
                            'MRR',
                            'NAME',
                            'EXTENDED_DESCRIPTION',
                            'PRODUCTLINEID',
                            'GLGROUP',
                            'ITEMTYPE'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            items = self.format_and_send_request(data)['data']['ITEM']
            total_items = total_items + items
            offset = offset + pagesize

        return total_items
