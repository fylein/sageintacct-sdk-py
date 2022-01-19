"""
Sage Intacct projects
"""
from .api_base import ApiBase


class Projects(ApiBase):
    """Class for Projects APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PROJECT')
