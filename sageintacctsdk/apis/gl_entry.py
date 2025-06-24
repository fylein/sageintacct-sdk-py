"""
Sage Intacct GL Entry
"""
from typing import Dict

from .api_base import ApiBase


class GLEntry(ApiBase):
    """Class for GL Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLENTRY')