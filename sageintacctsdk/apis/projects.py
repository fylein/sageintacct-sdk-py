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
        data = {
            'readByQuery': {
                'object': 'PROJECT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['project']
