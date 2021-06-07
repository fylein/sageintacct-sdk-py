"""
Sage Intacct tasks
"""
from typing import Dict

from .api_base import ApiBase


class Tasks(ApiBase):
    """Class for Tasks APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TASK')
