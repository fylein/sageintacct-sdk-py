"""
Sage Intacct contract lines
"""

from .api_base import ApiBase


class ContractLines(ApiBase):
    """Class for Contract Lines APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTRACTDETAIL')
