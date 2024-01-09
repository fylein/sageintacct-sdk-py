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
        return self.format_and_send_request(data)

    def post(self, data: Dict):
        """Post attachments to Sage Intacct.

        Returns:
            Dict of state of request with key.
        """
        data = {
            'create_supdoc': data
        }
        return self.format_and_send_request(data)

    def update(self, data: Dict):
        """Update attachments to Sage Intacct.

        Returns:
            Dict of state of request with key.
        """
        data = {
            'update_supdoc': data
        }
        return self.format_and_send_request(data)

    def get_folder(self, field: str, value: str):
        """Get attachment folder from Sage Intacct

        Parameters:
            field (str): A parameter to filter attachment folder by the field. (required).
            value (str): A parameter to filter attachment folder by the field - value. (required).

        Returns:
            Dict in Attachment Folder schema.
        """
        data = {
            'get_list': {
                '@object': 'supdocfolder',
                'filter': {
                    'expression': {
                        'field': field,
                        'operator': '=',
                        'value': value
                    }
                }
            }
        }

        return self.format_and_send_request(data)

    def get_attachment(self, field: str, value: str):
        """Get attachments from Sage Intacct

        Parameters:
            field (str): A parameter to filter attachments by the field. (required).
            value (str): A parameter to filter attachments by the field - value. (required).

        Returns:
            Dict in Attachments schema.
        """
        data = {
            'get_list': {
                '@object': 'supdoc',
                'filter': {
                    'expression': {
                        'field': field,
                        'operator': '=',
                        'value': value
                    }
                }
            }
        }

        return self.format_and_send_request(data)

    def get_all_folders(self):
        """Get all attachment folder from Sage Intacct

        Returns:
            List of Dict in Attachment Folder schema.
        """
        data = {
            'get_list': {
                '@object': 'supdocfolder'
            }
        }

        return self.format_and_send_request(data)['data']['supdocfolder']

    def get_all_attachments(self):
        """Get all attachments from Sage Intacct

        Returns:
            List of Dict in Attachment schema.
        """
        data = {
            'get_list': {
                '@object': 'supdoc'
            }
        }

        return self.format_and_send_request(data)['data']['supdoc']
