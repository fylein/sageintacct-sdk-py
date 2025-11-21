"""
Sage Intacct Tax solutions
"""
from typing import Dict

from .api_base import ApiBase


class TaxSolutions(ApiBase):
    """Class for TaxSolutions APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='TAXSOLUTION')
