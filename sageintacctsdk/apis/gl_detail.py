"""
Sage Intacct GL Detail
"""
from typing import Dict

from .api_base import ApiBase


class GLDetail(ApiBase):
    """Class for AP Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLDETAIL')

    def get_all(self):
        """Get all GL Detail records from Sage Intacct

        Returns:
            List of Dict in GL Detail schema.
        """
        data = {
            'readByQuery': {
                'object': 'GLDETAIL',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['gldetail']