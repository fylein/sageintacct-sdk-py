"""
Sage Intacct cost types
"""
from typing import Dict

from .api_base import ApiBase


class CostTypes(ApiBase):
    """Class for CostTypes APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='COSTTYPE')
