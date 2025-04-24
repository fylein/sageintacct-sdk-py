"""
Sage Intacct AR Invoice Items
"""

from typing import Dict, List, Optional, Union
from .api_base import ApiBase


class ARAging(ApiBase):
    """Class for AR Aging API."""
    def __init__(self):
        ApiBase.__init__(self)

    def get_araging(
        self,
        agingperiods: Union[str, List[str]],
        customerid: Optional[str] = None,
        showdetails: bool = False
    ) -> Dict:
        """
        Retrieve Accounts Receivable aging buckets via Sage Intacct's get_araging API.

        Parameters:
            agingperiods (str or list of str):  
                Either a comma-separated string of ranges (e.g. "31-60,61-90")  
                or a list like ["31-60","61-90","91-120","121-"].
            customerid (str, optional):  
                Single customer filter; pass None or "" to include all customers.
            showdetails (bool):  
                If True, returns line-level details; else returns summary buckets only.

        Returns:
            The parsed response under the "data" key (typically a dict of aging buckets).
        """
        # normalize the periods into a single comma-string
        if isinstance(agingperiods, (list, tuple)):
            periods = ",".join(agingperiods)
        else:
            periods = agingperiods

        # build payload
        data = {
            "get_araging": {
                "agingperiods": periods,
                "customerid": customerid or "",
                "showdetails": "true" if showdetails else "false"
            }
        }
        return self.format_and_send_request(data)['data']
