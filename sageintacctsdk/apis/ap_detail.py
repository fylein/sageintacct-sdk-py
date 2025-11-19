"""
Sage Intacct AP Detail
"""
from typing import Dict

from .api_base import ApiBase


class APDetail(ApiBase):
    """Class for AP Detail APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APDETAIL')