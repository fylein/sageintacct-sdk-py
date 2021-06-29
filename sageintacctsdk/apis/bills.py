"""
Sage Intacct bills
"""
from typing import Dict

from .api_base import ApiBase


class Bills(ApiBase):
    """Class for Bills APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APBILL')

    def update_attachment(self, recordno: str, supdocid: str):
        """Update bill with supdocid

        Parameters:
            recordno (str): A parameter to update bill by the recordno. (required).
            supdoc (str): A parameter to update attachment ID for the bill. (required).

        Returns:
            Dict in Bills update schema.
        """
        data = {
            'update': {
                'APBILL': {
                    'RECORDNO': recordno,
                    'SUPDOCID': supdocid
                }
            }
        }

        return self.format_and_send_request(data)
