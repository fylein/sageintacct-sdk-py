"""
Sage Intacct Order Entry Transactions
"""
from .api_base import ApiBase


class OrderEntryTransactions(ApiBase):
    """Class for Order Entry Transactions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='SODOCUMENT', post_legacy_method='create_sotransaction')