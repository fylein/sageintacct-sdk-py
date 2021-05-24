"""
Sage Intacct employees
"""
from typing import Dict

from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EMPLOYEE')

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
