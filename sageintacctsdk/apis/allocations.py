from .api_base import ApiBase

class Allocations(ApiBase):
    """Class for Allocation Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ALLOCATION')
