"""
Sage Intacct Dimensions
"""
from typing import Dict

from .api_base import ApiBase

class Dimensions(ApiBase):
    """Get all the Dimension from Sage Intact

    Returns:
        List of Dict of dimensions
    """
    def get_all(self):
        data = {
            'getDimensions': {}
        }

        return self.format_and_send_request(data)['data']['dimensions']['dimension']

    def get_objects(self):
        """Get all objects in a company
        
        Lists all standard and custom objects in a company, regardless of your permissions 
        or the company's subscriptions. This method now uses the inspect API.
        
        Returns:
            Dict containing object information
        """
        return self.inspect_objects()

    def inspect_objects(self, object_name: str = "*"):
        """Inspect objects in a company
        
        Lists all standard and custom objects in a company, regardless of your permissions 
        or the company's subscriptions.
        
        Parameters:
            object_name (str): The object name to inspect. Use "*" to return all objects. Defaults to "*".
            
        Returns:
            Dict containing object information
        """
        data = {
            'inspect': {
                'object': object_name
            }
        }

        return self.format_and_send_request(data)['data']
