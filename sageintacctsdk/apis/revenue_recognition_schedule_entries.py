"""
Sage Intacct Revenue Recognition Schedule Entry
"""
from typing import Dict

from .api_base import ApiBase


class RevRecScheduleEntries(ApiBase):
    """Class for Revenue Recognition Schedule Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REVRECSCHEDULEENTRY')

    def get_all(self):
        """Get all Revenue Recognition Schedule Entries from Sage Intacct

        Returns:
            List of Dict in Revenue Recognition Schedule Entry schema.
        """

        complete_data = []

        pagesize = '1000'
        data = {
            'readByQuery': {
                'object': 'REVRECSCHEDULEENTRY',
                'fields': '*',
                'query': None,
                'pagesize': pagesize
            }
        }
        firstResult = self.format_and_send_request(data)
        complete_data.extend(firstResult['data']['revrecscheduleentry'])

        numRemaining = firstResult['data']['@numremaining']
        resultId = firstResult['data']['@resultId']
        while int(numRemaining) > 0:
            data = {
                'readMore': {
                    'resultId': resultId
                }
            }
            nextResult = self.format_and_send_request(data)
            complete_data.extend(nextResult['data']['revrecscheduleentry'])
            numRemaining = nextResult['data']['@numremaining']
            resultId = nextResult['data']['@resultId']


        return complete_data
