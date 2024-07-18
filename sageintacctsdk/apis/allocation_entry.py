from .api_base import ApiBase

class AllocationEntry(ApiBase):
    """Class for Allocation Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='allocationentry')


    def get_all(self, field: str = None, value: str = None, fields: list = None, keys: list = None):

        data = {
            'readByQuery': {
                'object': 'allocationentry',
                'fields': '*',
                'query': f"ALLOCATIONID in ({','.join(f"'{k}'" for k in keys)})" if keys else None,
                'pagesize': '1000'
            }
        }

        print(data)

        return self.format_and_send_request(data=data)
