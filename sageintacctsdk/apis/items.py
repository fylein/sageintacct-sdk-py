"""
Sage Intacct items
"""
from typing import Dict

from .api_base import ApiBase


class Items(ApiBase):
    """Class for Items APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ITEM')
