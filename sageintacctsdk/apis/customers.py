"""
Sage Intacct customers
"""
from .api_base import ApiBase


class Customers(ApiBase):
    """Class for Customers APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CUSTOMER')
