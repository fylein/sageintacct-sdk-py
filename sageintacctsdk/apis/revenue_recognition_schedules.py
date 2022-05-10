"""
Sage Intacct Revenue Recognition Schedule
"""
from typing import Dict

from .api_base import ApiBase


class RevRecSchedules(ApiBase):
    """Class for Revenue Recognition Schedule Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REVRECSCHEDULE')
