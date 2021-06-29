"""
Sage Intacct expense reports
"""
from typing import Dict

from .api_base import ApiBase


class ExpenseReports(ApiBase):
    """Class for Expense Reports APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EEXPENSES')

    def update_attachment(self, key: str, supdocid: str):
        """
        Update expense reports with supdocid
        Parameters:
            key (str): A parameter to update expense reports by the key. (required).
            supdoc (str): A parameter to update attachment ID for the expense report. (required).
        Returns:
            Dict in Expense Reports update schema.
        """
        data = {
            'update_expensereport': {
                '@key': key,
                'supdocid': supdocid
            }
        }
        return self.format_and_send_request(data)
