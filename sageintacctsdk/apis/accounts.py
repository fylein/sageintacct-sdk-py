"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCOUNT')
