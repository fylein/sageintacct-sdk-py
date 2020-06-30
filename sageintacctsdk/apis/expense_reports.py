"""
Sage Intacct expense reports
"""
from typing import Dict

from .api_base import ApiBase


class ExpenseReports(ApiBase):
    """Class for Expense Reports APIs."""

    def post(self, data: Dict):
        """Post expense reports to Sage Intacct.

        Returns:
            Dict of state of request with key.
        """
        data = {
            'create_expensereport': data
        }
        return self._format_post_request(data)
