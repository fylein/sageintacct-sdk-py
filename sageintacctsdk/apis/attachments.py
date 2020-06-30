"""
Sage Intacct attachments
"""
from typing import Dict

from .api_base import ApiBase


class Attachments(ApiBase):
    """Class for Attachments APIs."""

    def create_attachments_folder(self, data: Dict):
        """Post attachment folder to Sage Intacct.

        Returns:
            Dict of state of request with key.
        """
        data = {
            'create_supdocfolder': data
        }
        return self._format_post_request(data)

    def post(self, data: Dict):
        """Post attachments to Sage Intacct.

        Returns:
            Dict of state of request with key.
        """
        data = {
            'create_supdoc': data
        }
        return self._format_post_request(data)
