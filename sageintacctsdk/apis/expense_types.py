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
