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

        yield from super().get_all_generator(fields=allocation_entries_fields, field=field, value=value)
