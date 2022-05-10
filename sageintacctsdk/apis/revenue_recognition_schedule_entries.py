"""
Sage Intacct Revenue Recognition Schedule Entry
"""
from typing import Dict

from .api_base import ApiBase


class RevRecScheduleEntries(ApiBase):
    """Class for Revenue Recognition Schedule Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REVRECSCHEDULEENTRY')
