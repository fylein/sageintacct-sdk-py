"""
Sage Inventory Control Price List Entries
"""

from .api_base import ApiBase


class InventoryControlPriceListEntries(ApiBase):
    """Class for Inventory Control Price List Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='INVPRICELISTENTRY')
