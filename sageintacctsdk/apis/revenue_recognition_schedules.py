"""
Sage Intacct Revenue Recognition Schedule
"""
from typing import Dict

from .api_base import ApiBase


class RevRecSchedules(ApiBase):
    """Class for Revenue Recognition Schedule APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REVRECSCHEDULE')

    def get_all(self):
        """Get all Revenue Recognition Schedules from Sage Intacct

        Returns:
            List of Dict in Revenue Recognition Schedules schema.
        """

        complete_data = []

        pagesize = '1000'
        data = {
            'readByQuery': {
                'object': 'REVRECSCHEDULE',
                'fields': '*',
                'query': None,
                'pagesize': pagesize
            }
        }
        firstResult = self.format_and_send_request(data)
        complete_data.extend(firstResult['data']['revrecschedule'])

        numRemaining = firstResult['data']['@numremaining']
        resultId = firstResult['data']['@resultId']
        while int(numRemaining) > 0:
            data = {
                'readMore': {
                    'resultId': resultId
                }
            }
            nextResult = self.format_and_send_request(data)
            complete_data.extend(nextResult['data']['revrecschedule'])
            numRemaining = nextResult['data']['@numremaining']
            resultId = nextResult['data']['@resultId']

        return complete_data
