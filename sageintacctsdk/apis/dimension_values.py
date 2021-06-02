"""
Sage Intacct Dimensions Values
"""
from typing import Dict

from .api_base import ApiBase

class DimensionValues(ApiBase):
    def count(self, dimension_name: str):
        get_count = {
            'query': {
                'object': dimension_name,
                'select': {
                    'field': 'id'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        return int(response['data']['@totalcount'])

    def get_all(self, dimension_name: str):
        """Get all values of given dimension from Sage Intacct

        Parameters:
            dimension_name (str): Dimension name.

        Returns:
            List of Dict of Values of Dimensions
        """
        total_user_dimensions = []
        count = self.count(dimension_name)

        pagesize = 2000
        for offset in range(0, count, pagesize):
            data = {
                'query': {
                    'object': dimension_name,
                    'select': {
                        'field': {
                            'name',
                            'createdBy',
                            'updatedBy',
                            'id'
                        }
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }

            user_dimensions = self.format_and_send_request(data)['data'][dimension_name]
            total_user_dimensions.extend(user_dimensions)

        return total_user_dimensions
