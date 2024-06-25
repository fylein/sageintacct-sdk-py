"""
Sage Intacct contracts
"""

from .api_base import ApiBase


class Contracts(ApiBase):
    """Class for Contracts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACT')
