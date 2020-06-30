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
        return self._format_post_request(data)

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

        return self._format_post_request(data)['data']['employee']
