"""
Sage Intacct expense types
"""
from typing import Dict

from .api_base import ApiBase


class ExpenseTypes(ApiBase):
    """Class for Expense Types APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='EEACCOUNTLABEL')
