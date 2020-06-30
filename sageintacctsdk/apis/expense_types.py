"""
Sage Intacct expense types
"""
from typing import Dict

from .api_base import ApiBase


class ExpenseTypes(ApiBase):
    """Class for Expense Types APIs."""

    def post(self, data: Dict):
        """Post expense types to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'EEACCOUNTLABEL': data
            }
        }
        return self._format_post_request(data)

    def get_all(self):
        """Get all expense types from Sage Intacct

        Returns:
            List of Dict in Expense Types schema.
        """
        data = {
            'readByQuery': {
                'object': 'EEACCOUNTLABEL',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self._format_post_request(data)['data']['eeaccountlabel']
