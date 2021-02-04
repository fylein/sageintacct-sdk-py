"""
Sage Intacct Reimbursements
"""
from typing import Dict

from .api_base import ApiBase


class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""

    def post(self, data: Dict):
        """Post Reimbursements to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create_reimbursementrequest': data
        }
        return self.format_and_send_request(data)

    def get(self, field: str, value: str):
        """Get Reimbursement from Sage Intacct

        Parameters:
            field (str): A parameter to filter Reimbursement by the field. (required).
            value (str): A parameter to filter Reimbursement by the field - value. (required).

        Returns:
            Dict in Reimbursement schema.
        """
        data = {
            'readByQuery': {
                'object': 'EPPAYMENT',
                'fields': '*',
                'query': "{0} = '{1}'".format(field, value),
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['eppayment']

    def get_all(self):
        """Get all Reimbursements from Sage Intacct

        Returns:
            List of Dict in Reimbursements schema.
        """
        data = {
            'readByQuery': {
                'object': 'EPPAYMENT',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['eppayment']
