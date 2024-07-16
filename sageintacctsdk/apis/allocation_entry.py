from .api_base import ApiBase

class AllocationEntry(ApiBase):
    """Class for Allocation Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='allocationentry')


    def get_all_generator(self):

        """
        Get all the allocation entries.
        """

        data = {
            'readByQuery': {
                'object': 'ALLOCATIONENTRY',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        yield self.format_and_send_request(data)['data']
