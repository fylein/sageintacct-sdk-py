"""
Sage Intacct bills
"""
from typing import Dict

from .api_base import ApiBase


class Bills(ApiBase):
    """Class for Bills APIs."""

    def post(self, data: Dict):
        """Post bills to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'APBILL': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get bills from Sage Intacct

        Parameters:
            field (str): A parameter to filter bills by the field. (required).
            value (str): A parameter to filter bills by the field - value. (required).

        Returns:
            Dict in bills schema.
        """
        data = {
            'readByQuery': {
                'object': 'APBILL',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all bills from Sage Intacct

        Returns:
            List of Dict in Bills schema.
        """
        data = {
            'readByQuery': {
                'object': 'APBILL',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['apbill']

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
