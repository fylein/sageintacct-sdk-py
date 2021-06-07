"""
Sage Intacct vendors
"""
from typing import Dict

from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Vendors APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='VENDOR')
