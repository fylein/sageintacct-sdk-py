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
        return self._format_post_request(data)
