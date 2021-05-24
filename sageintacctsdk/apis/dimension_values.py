"""
Sage Intacct Dimensions Values
"""
from typing import Dict

from .api_base import ApiBase

class DimensionValues(ApiBase):

    def get(self, dimension_name: str):
        """Get all values of given dimension from Sage Intacct
        
        Returns:
            List of Dict of Values of Dimensions
        """
        
        total_user_dimensions = []
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
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
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
            total_user_dimensions = total_user_dimensions +  user_dimensions
            offset = offset + pagesize
        
        return total_user_dimensions
