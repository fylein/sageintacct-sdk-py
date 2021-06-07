"""
Sage Intacct contacts
"""
from typing import Dict

from .api_base import ApiBase


class Contacts(ApiBase):
    """Class for Contacts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CONTACT')
