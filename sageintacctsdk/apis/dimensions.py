"""
Sage Intacct Dimensions
"""
from typing import Dict

from .api_base import ApiBase

class Dimensions(ApiBase):
    """Get all the Dimension from Sage Intact

    Returns:
        List of Dict of dimensions
    """

    def get(self):

        data = {
            'Dimensions': {}
        }

        return self.format_and_send_request(data)['data']['dimensions']
