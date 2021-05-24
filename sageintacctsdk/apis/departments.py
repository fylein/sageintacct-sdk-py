"""
Sage Intacct departments
"""
from typing import Dict

from .api_base import ApiBase


class Departments(ApiBase):
    """Class for Departments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='DEPARTMENT')
