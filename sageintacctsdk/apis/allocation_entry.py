import re

from sageintacctsdk.exceptions import WrongParamsError
from .api_base import ApiBase

class AllocationEntry(ApiBase):
    """Class for Allocation Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='allocationentry')


    def get_all_generator(self, field: str = None, value: str = None, fields: list = None, updated_at: str = None, order_by_field: str = None, order: str = None):

        """
        Get all the allocation entries.
        """

        allocation_entries_fields = ['ALLOCATIONID', 'ALLOCATIONKEY', 'LOCATIONID', 'DEPARTMENTID', 'PROJECTID',
                                    'CUSTOMERID', 'ITEMID', 'TASKID', 'COSTTYPEID', 'CLASSID']
        user_defined_dimensions = []

        fields = self.get_lookup()
        if fields and 'Type' in fields and fields['Type'] and 'Relationships' in fields['Type'] and fields['Type']['Relationships'] and 'Relationship' in fields['Type']['Relationships']:
            user_defined_dimensions = fields['Type']['Relationships']['Relationship']
 
        for allocation_field in user_defined_dimensions:
            allocation_entries_fields.append(allocation_field['RELATEDBY'])

        try:
            yield from super().get_all_generator(fields=allocation_entries_fields, field=field, value=value)
        except WrongParamsError as e:
            error_response = e.response
            if error_response is None:
                raise
            description2 = ''
            if 'error' in error_response and isinstance(error_response['error'], list) and error_response['error']:
                error = error_response['error'][0]
                if 'description2' in error:
                    description2 = error['description2']
            
            if description2:
                match = re.search(r'\n\tallocationentry: \[(.*?)\]', description2)
                if match:
                    removable_fields = match.group(1).split(', ')
                    for remove_field in removable_fields:
                        allocation_entries_fields.remove(remove_field)
                    yield from super().get_all_generator(fields=allocation_entries_fields, field=field, value=value)
            else:
                raise
