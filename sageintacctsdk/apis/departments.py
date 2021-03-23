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
        total_departments = []
        get_count = {
            'query': {
                'object': 'DEPARTMENT',
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
                    'object': 'DEPARTMENT',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'DEPARTMENTID',
                            'TITLE',
                            'PARENTKEY',
                            'PARENTID',
                            'SUPERVISORNAME',
                            'STATUS',
                            'CUSTTITLE'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            departments = self.format_and_send_request(data)['data']['DEPARTMENT']
            total_departments = total_departments + departments
            offset = offset + pagesize

        return total_departments
