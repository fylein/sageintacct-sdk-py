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
        total_employees = []
        get_count = {
            'query': {
                'object': 'EMPLOYEE',
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
                    'object': 'EMPLOYEE',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'EMPLOYEEID',
                            'SSN',
                            'TITLE',
                            'LOCATIONID',
                            'DEPARTMENTID',
                            'STATUS',
                            'EMPLOYEETYPE',
                            'GENDER',
                            'CURRENCY',
                            'ACHENABLED'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            employees = self.format_and_send_request(data)['data']['EMPLOYEE']
            total_employees = total_employees + employees
            offset = offset + pagesize

        return total_employees
