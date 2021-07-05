"""
Sage Intacct Location Entities
"""
from typing import Dict

from .api_base import ApiBase


class LocationEntities(ApiBase):
    """Class for Location Entities APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='LOCATIONENTITY')
