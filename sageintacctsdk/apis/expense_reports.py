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
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get expense reports from Sage Intacct

        Parameters:
            field (str): A parameter to filter expense reports by the field. (required).
            value (str): A parameter to filter expense reports by the field - value. (required).

        Returns:
            Dict in Expense Reports schema.
        """
        data = {
            'query': {
                'object': 'EEXPENSES',
                'select': {
                    'field': [
                        'RECORDNO',
                        'RECORDID',
                        'WHENCREATED',
                        'WHENPOSTED',
                        'TOTALENTERED',
                        'STATE',
                        'TOTALDUE',
                        'DESCRIPTION',
                        'CURRENCY',
                        'BASECURR',
                        'MEMO'
                    ]
                },
                'filter': {
                    'equalto': {
                        'field': field,
                        'value': value
                    }
                },
                'pagesize': '2000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all expense reports from Sage Intacct

        Returns:
            List of Dict in Expense Reports schema.
        """
        total_expense_reports = []
        get_count = {
            'query': {
                'object': 'EEXPENSES',
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
                    'object': 'EEXPENSES',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'RECORDID',
                            'WHENCREATED',
                            'WHENPOSTED',
                            'TOTALENTERED',
                            'STATE',
                            'TOTALDUE',
                            'DESCRIPTION',
                            'CURRENCY',
                            'BASECURR',
                            'MEMO'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            expense_reports = self.format_and_send_request(data)['data']['EEXPENSES']
            total_expense_reports = total_expense_reports + expense_reports
            offset = offset + pagesize
        return total_expense_reports

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
