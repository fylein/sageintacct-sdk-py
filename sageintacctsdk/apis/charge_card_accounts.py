"""
Sage Intacct charge card accounts
"""
from typing import Dict

from .api_base import ApiBase


class ChargeCardAccounts(ApiBase):
    """Class for Charge Card Accounts APIs."""

    def get(self, id: str):
        """Get charge card account from Sage Intacct

        Parameters:
            id (str): A parameter to get charge card account by the CARDID. (required).

        Returns:
            Dict in Charge Card Account schema.
        """
        data = {
            'readByName': {
                'object': 'CREDITCARD',
                'keys': id,
                'fields': '*'
            }
        }

        return self.format_and_send_request(data)['data']

    def get_all(self):
        """Get all charge card accounts from Sage Intacct

        Returns:
            List of Dict in Charge Card schema.
        """
        total_charge_card_accounts = []
        get_count = {
            'query': {
                'object': 'CREDITCARD',
                'select': {
                    'field': 'RECORDNO'
                },
                'filter': {
                    'equalto': {
                        'field': 'LIABILITYTYPE',
                        'value': 'Credit'
                    }
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'CREDITCARD',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'CARDID',
                            'DESCRIPTION',
                            'CARDTYPE',
                            'EXP_MONTH',
                            'EXP_YEAR',
                            'COMMCARD',
                            'STATUS',
                            'VENDORID',
                            'DEPT',
                            'LOCATION',
                            'LIABILITYTYPE',
                            'OUTSOURCECARD'
                        ]
                    },
                    'filter': {
                        'equalto': {
                            'field': 'LIABILITYTYPE',
                            'value': 'Credit'
                        }
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            charge_card_accounts = self.format_and_send_request(data)['data']['CREDITCARD']
            total_charge_card_accounts = total_charge_card_accounts + charge_card_accounts
            offset = offset + pagesize

        return total_charge_card_accounts
