"""
Sage Intacct Expense Custom Fields
"""
from typing import Dict

from .api_base import ApiBase

class GetDimensions(ApiBase):

    def get(self):

        data = {
            'getDimensions': {}
        }

        return self.format_and_send_request(data)['data']['dimensions']
