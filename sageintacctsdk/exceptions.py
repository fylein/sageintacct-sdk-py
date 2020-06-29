"""
Sage Intacct SDK Exceptions
"""


class SageIntacctSDKError(Exception):
    """The base exception class for SAGEINTACCTSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(SageIntacctSDKError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class ExpiredSessionError(SageIntacctSDKError):
    """Expired (old) session id, 498 error."""


class InvalidSessionError(SageIntacctSDKError):
    """Wrong/non-existing session id, 401 error."""


class WrongParamsError(SageIntacctSDKError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""


class NotFoundItemError(SageIntacctSDKError):
    """Not found the item from URL, 404 error."""


class InternalServerError(SageIntacctSDKError):
    """The rest SAGEINTACCTSDK errors, 500 error."""
