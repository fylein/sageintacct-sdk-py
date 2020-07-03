"""
Sage Intacct employees
"""
from typing import Dict

from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    def post(self, data: Dict):
        """Post employee to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'EMPLOYEE': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get location from Sage Intacct

        Parameters:
            field (str): A parameter to filter employees by the field. (required).
            value (str): A parameter to filter employees by the field - value. (required).

        Returns:
            Dict in Location schema.
        """
        data = {
            'readByQuery': {
                'object': 'EMPLOYEE',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all employees from Sage Intacct

        Returns:
            List of Dict in Employee schema.
        """
        data = {
            'readByQuery': {
                'object': 'EMPLOYEE',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['employee']
