"""
Sage Intacct Journal Entries
"""
from typing import Dict

from .api_base import ApiBase


class JournalEntries(ApiBase):
    """Class for Journal Entries APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLBATCH')

    def update_attachment(self, recordno: str, supdocid: str):
        """Update journal entry with supdocid

        Parameters:
            recordno (str): A parameter to update journal entry by the recordno. (required).
            supdoc (str): A parameter to update attachment ID for the journal entry. (required).

        Returns:
            Dict in Journal update schema.
        """
        data = {
            'update': {
                'GLBATCH': {
                    'RECORDNO': recordno,
                    'SUPDOCID': supdocid
                }
            }
        }

        return self.format_and_send_request(data)
