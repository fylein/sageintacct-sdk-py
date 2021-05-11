"""
Sage Intacct tasks
"""
from typing import Dict

from .api_base import ApiBase


class Tasks(ApiBase):
    """Class for Tasks APIs."""

    def post(self, data: Dict):
        """Post tasks to Sage Intacct.

        Returns:
            Dict of state of request with RECORDNO.
        """
        data = {
            'create': {
                'TASK': data
            }
        }
        return self.format_and_send_request(data)

    def get_all(self):
        """Get all tasks from Sage Intacct

        Returns:
            List of Dict in Tasks schema.
        """
        total_tasks = []
        get_count = {
            'query': {
                'object': 'TASK',
                'select': {
                    'field': 'RECORDNO'
                },
                'pagesize': '1'
            }
        }

        response = self.format_and_send_request(get_count)
        count = int(response['data']['@totalcount'])
        pagesize = 2000
        offset = 0
        for i in range(0, count, pagesize):
            data = {
                'query': {
                    'object': 'TASK',
                    'select': {
                        'field': [
                            'RECORDNO',
                            'TASKID',
                            'PARENTKEY',
                            'PARENTID',
                            'NAME',
                            'PARENTTASKNAME',
                            'PROJECTKEY',
                            'PROJECTID',
                            'PROJECTNAME',
                            'ITEMKEY',
                            'ITEMID',
                            'ITEMNAME',
                            'DESCRIPTION',
                            'BILLABLE',
                            'TASKNO',
                            'TASKSTATUS',
                            'CLASSID',
                            'CLASSNAME',
                            'CLASSKEY',
                            'ROOTPARENTKEY',
                            'ROOTPARENTID',
                            'ROOTPARENTNAME'
                        ]
                    },
                    'pagesize': pagesize,
                    'offset': offset
                }
            }
            tasks = self.format_and_send_request(data)['data']['TASK']
            total_tasks = total_tasks + tasks
            offset = offset + pagesize

        return total_tasks
