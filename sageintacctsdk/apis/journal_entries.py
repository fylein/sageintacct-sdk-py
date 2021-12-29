"""
Sage Intacct Journal Entries
"""
from typing import Dict

from .api_base import ApiBase


class JournalEntries(ApiBase):
    """Class for Journal Entries APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLBATCH')
