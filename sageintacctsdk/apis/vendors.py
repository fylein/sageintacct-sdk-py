"""
Sage Intacct vendors
"""
from typing import Dict

from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Vendors APIs."""

    def post(self, data: Dict):
        """Post vendors to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'VENDOR': data
            }
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get vendors from Sage Intacct

        Parameters:
            field (str): A parameter to filter vendors by the field. (required).
            value (str): A parameter to filter vendors by the field - value. (required).

        Returns:
            Dict in vendors schema.
        """
        data = {
            'readByQuery': {
                'object': 'VENDOR',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all vendors from Sage Intacct

        Returns:
            List of Dict in Vendors schema.
        """
        total_vendors = []
        get_count = {
            'query': {
                'object': 'VENDOR',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])

        offset = 0
        page_size = 2000

        for i in range(0, count, page_size):
            data = {
                'query': {
                    'object': 'VENDOR',
                    'select': {
                        'field': {
                            'RECORDNO',
                            'NAME',
                            'VENDORID',
                            'PARENTKEY',
                            'PARENTID',
                            'PARENTNAME',
                            'DISPLAYCONTACT.CONTACTNAME',
                            'DISPLAYCONTACT.COMPANYNAME',
                            'DISPLAYCONTACT.FIRSTNAME',
                            'DISPLAYCONTACT.LASTNAME',
                            'DISPLAYCONTACT.INITIAL',
                            'DISPLAYCONTACT.PRINTAS',
                            'DISPLAYCONTACT.PHONE1',
                            'DISPLAYCONTACT.PHONE2',
                            'DISPLAYCONTACT.EMAIL1',
                            'DISPLAYCONTACT.EMAIL2',
                            'VENDORACCOUNTNO',
                            'VENDTYPE',
                            'ACCOUNTLABEL',
                            'APACCOUNT',
                            'APACCOUNTTITLE',
                            'STATUS'
                        }
                    },
                    'pagesize': page_size,
                    'offset': offset
                }
            }
            vendors = self.format_and_send_request(data)['data']['VENDOR']
            total_vendors = total_vendors + vendors
            offset = offset + page_size

        return total_vendors
