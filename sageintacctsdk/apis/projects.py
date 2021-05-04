"""
Sage Intacct projects
"""
from typing import Dict

from .api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""

    def post(self, data: Dict):
        """Post projects to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'PROJECT': data
            }
        }
        return self.format_and_send_request(data)

    def count(self):
        get_count = {
            'query': {
                'object': 'PROJECT',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        return int(response['data']['@totalcount'])

    def get(self, field: str, value: str):
        """Get projects from Sage Intacct

        Parameters:
            field (str): A parameter to filter projects by the field. (required).
            value (str): A parameter to filter projects by the field - value. (required).

        Returns:
            Dict in projects schema.
        """
        data = {
            'readByQuery': {
                'object': 'PROJECT',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all projects from Sage Intacct

        Returns:
            List of Dict in Projects schema.
        """
        total_projects = []
        count = self.count()

        offset = 0
        page_size = 2000

        for i in range(0, count, page_size):
            data = {
                'query': {
                    'object': 'PROJECT',
                    'select': {
                        'field': {
                            'RECORDNO',
                            'PROJECTID',
                            'NAME',
                            'DESCRIPTION',
                            'CURRENCY',
                            'PROJECTCATEGORY',
                            'PROJECTSTATUS',
                            'PARENTKEY',
                            'PARENTID',
                            'PARENTNAME',
                            'STATUS',
                            'CUSTOMERKEY',
                            'CUSTOMERID',
                            'CUSTOMERNAME',
                            'PROJECTTYPE',
                            'DEPARTMENTNAME',
                            'LOCATIONID',
                            'LOCATIONNAME',
                            'BUDGETID',
                            'MEGAENTITYID',
                            'MEGAENTITYNAME'
                        }
                    },
                    'pagesize': page_size,
                    'offset': offset
                }
            }
            projects = self.format_and_send_request(data)['data']['PROJECT']
            total_projects = total_projects + projects
            offset = offset + page_size

        return total_projects
