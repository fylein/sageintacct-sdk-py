"""
Sage Intacct AR Invoice Items
"""

from .api_base import ApiBase


class ARInvoiceItems(ApiBase):
    """Class for AR Invoice Items APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARINVOICEITEM')
