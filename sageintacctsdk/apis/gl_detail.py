"""
Sage Intacct GL Detail
"""
from typing import Dict

from .api_base import ApiBase


class GLDetail(ApiBase):
    """Class for GL Detail APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLDETAIL')