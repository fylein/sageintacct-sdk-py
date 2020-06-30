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

    def get_all(self):
        """Get all contacts from Sage Intacct

        Returns:
            List of Dict in Contacts schema.
        """
        total_contacts = []
        get_count = {
            'query': {
                'object': 'CONTACT',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self._format_post_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'CONTACT',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'CONTACTNAME',
                            'COMPANYNAME',
                            'FIRSTNAME',
                            'LASTNAME',
                            'INITIAL',
                            'PRINTAS',
                            'TAXABLE',
                            'MAILADDRESS.ADDRESS1'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            contacts = self._format_post_request(data)['data']['CONTACT']
            total_contacts = total_contacts + contacts
            offset = offset + pagesize
        return total_contacts
