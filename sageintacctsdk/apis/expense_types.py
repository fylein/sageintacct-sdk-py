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
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get expense types from Sage Intacct

        Parameters:
            field (str): A parameter to filter expense types by the field. (required).
            value (str): A parameter to filter expense types by the field - value. (required).

        Returns:
            Dict in Location schema.
        """
        data = {
            'readByQuery': {
                'object': 'EEACCOUNTLABEL',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

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

        return self.format_and_send_request(data)['data']['eeaccountlabel']
