"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Accounts APIs."""

    def post(self, data: Dict):
        """Post general ledger account to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'GLACCOUNT': data
            }
        }
        return self._format_post_request(data)
