"""
Sage Intacct departments
"""
from typing import Dict

from .api_base import ApiBase


class Departments(ApiBase):
    """Class for Departments APIs."""

    def post(self, data: Dict):
        """Post departments to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'DEPARTMENT': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get departments from Sage Intacct

        Parameters:
            field (str): A parameter to filter departments by the field. (required).
            value (str): A parameter to filter departments by the field - value. (required).

        Returns:
            Dict in Departments schema.
        """
        data = {
            'readByQuery': {
                'object': 'DEPARTMENT',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all departments from Sage Intacct

        Returns:
            List of Dict in Departments schema.
        """
        data = {
            'readByQuery': {
                'object': 'DEPARTMENT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['department']
