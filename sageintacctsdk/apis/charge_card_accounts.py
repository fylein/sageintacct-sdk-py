"""
Sage Intacct charge card accounts
"""
from typing import Dict

from .api_base import ApiBase


class ChargeCardAccounts(ApiBase):
    """Class for Charge Card Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CREDITCARD')
