"""
Sage Intacct Expense Payment Types
"""
from typing import Dict

from .api_base import ApiBase


class ExpensePaymentTypes(ApiBase):
    """Class for Expense Payment Types APIs."""

    def post(self, data: Dict):
        """Post Expense Payment Type to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'EXPENSEPAYMENTTYPE': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get Expense Payment Types from Sage Intacct

        Parameters:
            field (str): A parameter to filter Expense Payment Types by the field. (required).
            value (str): A parameter to filter Expense Payment Types by the field - value. (required).

        Returns:
            Dict in Expense Payment Types schema.
        """
        data = {
            'readByQuery': {
                'object': 'EXPENSEPAYMENTTYPE',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all Expense Payment Types from Sage Intacct

        Returns:
            List of Dict in Expense Payment Types schema.
        """
        total_expense_payment_types = []
        get_count = {
            'query': {
                'object': 'EXPENSEPAYMENTTYPE',
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
        for _ in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'EXPENSEPAYMENTTYPE',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'NAME',
                            'DESCRIPTION',
                            'NONREIMBURSABLE',
                            'OFFSETACCTNO',
                            'OFFSETACCTTITLE',
                            'STATUS',
                            'WHENCREATED',
                            'WHENMODIFIED',
                            'CREATEDBY',
                            'MODIFIEDBY',
                            'MEGAENTITYKEY',
                            'MEGAENTITYID',
                            'MEGAENTITYNAME'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            expense_payment_types = self.format_and_send_request(data)['data']['EXPENSEPAYMENTTYPE']
            total_expense_payment_types = total_expense_payment_types + expense_payment_types
            offset = offset + pagesize

        return total_expense_payment_types
