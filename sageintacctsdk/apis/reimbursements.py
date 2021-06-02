"""
Sage Intacct Reimbursements
"""
from typing import Dict

from .api_base import ApiBase


class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EPPAYMENT', post_legacy_method='create_reimbursementrequest')

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
