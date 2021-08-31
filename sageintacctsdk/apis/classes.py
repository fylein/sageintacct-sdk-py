"""
Sage Intacct classes
"""
from typing import Dict

from .api_base import ApiBase


class Classes(ApiBase):
    """Class for Sage Intacct Classes APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CLASS')
