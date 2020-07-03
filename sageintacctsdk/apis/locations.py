"""
Sage Intacct locations
"""
from typing import Dict

from .api_base import ApiBase


class Locations(ApiBase):
    """Class for Locations APIs."""

    def post(self, data: Dict):
        """Post location to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'LOCATION': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get location from Sage Intacct

        Parameters:
            field (str): A parameter to filter locations by the field. (required).
            value (str): A parameter to filter locations by the field - value. (required).

        Returns:
            Dict in Location schema.
        """
        data = {
            'readByQuery': {
                'object': 'LOCATION',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all locations from Sage Intacct

        Returns:
            List of Dict in Locations schema.
        """
        data = {
            'readByQuery': {
                'object': 'LOCATION',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['location']
