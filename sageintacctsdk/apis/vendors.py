"""
Sage Intacct vendors
"""
from typing import Dict

from .api_base import ApiBase
from .constants import dimensions_fields_mapping


class Vendors(ApiBase):
    """Class for Vendors APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='VENDOR')

    def get(self, field: str, value: str, fields: list = None):
        """Get data from Sage Intacct based on filter.

        Parameters:
            field (str): A parameter to filter by the field. (required).
            value (str): A parameter to filter by the field - value. (required).

        Returns:
            Dict.
        """
        data = {
            'query': {
                'object': 'VENDOR',
                'select': 
                    {
                        'field': fields if fields else dimensions_fields_mapping['VENDOR'],
                    },
                'pagesize': '1000',
                'filter': {
                    'equalto': [
                    {
                        'field': field,
                        'value': value
                    }]
                }
            }
        }

        return self.format_and_send_request(data)['data']