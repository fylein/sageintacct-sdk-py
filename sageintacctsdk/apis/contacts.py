"""
Sage Intacct contacts
"""
from typing import Dict

from .api_base import ApiBase


class Contacts(ApiBase):
    """Class for Contacts APIs."""

    def post(self, data: Dict):
        """Post contact to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'CONTACT': data
            }
        }
        return self._format_post_request(data)
