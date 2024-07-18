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

        fields = self.get_lookup()
        if fields:
            fields = fields['Type']['Relationships']['Relationship']

        for allocation_field in fields:
            allocation_entries_fields.append(allocation_field['RELATEDBY'])

        yield from super().get_all_generator(fields=allocation_entries_fields, field=field, value=value)
