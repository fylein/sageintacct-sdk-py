"""
API Base class with util functions
"""
import json
import datetime
import uuid
from typing import Dict

import xmltodict
import requests

from ..exceptions import *

class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self.__access_token = None
        self.__sender_id = None
        self.__sender_password = None
        self.__session_id = None
        self.__api_url = 'https://api.intacct.com/ia/xml/xmlgw.phtml'

    def set_sender_id(self, sender_id: str):
        """
        Set the sender id for APIs
        :param sender_id: sender id
        :return: None
        """
        self.__sender_id = sender_id

    def set_sender_password(self, sender_password: str):
        """
        Set the sender password for APIs
        :param sender_password: sender id
        :return: None
        """
        self.__sender_password = sender_password

    def _get_session_id(self, user_id: str, company_id: str, user_password: str):
        """
        Sets the session id for APIs
        :param access_token: acceess token (JWT)
        :return: session id
        """

        timestamp = datetime.datetime.now()
        dict_body = {
            'request': {
                'control': {
                    'senderid': self.__sender_id,
                    'password': self.__sender_password,
                    'controlid': timestamp,
                    'uniqueid': False,
                    'dtdversion': 3.0,
                    'includewhitespace': False
                },
                'operation': {
                    'authentication': {
                        'login': {
                            'userid': user_id,
                            'companyid': company_id,
                            'password': user_password
                        }
                    },
                    'content': {
                        'function': {
                            '@controlid': str(uuid.uuid4()),
                            'getAPISession': None
                        }
                    }
                }
            }
        }

        response = self._post_request(dict_body, self.__api_url)

        if response['authentication']['status'] == 'success':
            session_details = response['result']['data']['api']
            self.__api_url = session_details['endpoint']
            self.__session_id = session_details['sessionid']

            return self.__session_id

        else:
            raise SageIntacctSDKError('Error: {0}'.format(response['errormessage']))

    def set_session_id(self, session_id: str):
        """
        Set the session id for APIs
        :param session_id: session id
        :return: None
        """
        self.__session_id = session_id

    def _post_request(self, dict_body: dict, api_url: str):
        """Create a HTTP post request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'content-type': 'application/xml'
        }
        body = xmltodict.unparse(dict_body)

        response = requests.post(api_url, headers=api_headers, data=body)

        parsed_xml = xmltodict.parse(response.text)
        parsed_response = json.loads(json.dumps(parsed_xml))

        if response.status_code == 200:
            if parsed_response['response']['control']['status'] == 'success':
                api_response = parsed_response['response']['operation']

            if parsed_response['response']['control']['status'] == 'failure':
                raise WrongParamsError('Some of the parameters are wrong', parsed_response['response']['errormessage'])

            if api_response['result']['status'] == 'success':
                return api_response

            if api_response['result']['status'] == 'failure':
                raise WrongParamsError('Error during {0}'.format(api_response['result']['function']), '{0}'.format(api_response['result']['errormessage']))

        if response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', parsed_response)

        if response.status_code == 401:
            raise InvalidTokenError('Invalid token / Incorrect credentials', parsed_response)

        if response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', parsed_response)

        if response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', parsed_response)

        if response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', parsed_response)

        if response.status_code == 500:
            raise InternalServerError('Internal server error', parsed_response)

        raise SageIntacctSDKError('Error: {0}'.format(parsed_response))

    def format_and_send_request(self, data: Dict):
        """Format data accordingly to convert them to xml.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.

        Returns:
            A response from the _post_request (dict).
        """

        key = next(iter(data))
        timestamp = datetime.datetime.now()

        dict_body = {
            'request': {
                'control': {
                    'senderid': self.__sender_id,
                    'password': self.__sender_password,
                    'controlid': timestamp,
                    'uniqueid': False,
                    'dtdversion': 3.0,
                    'includewhitespace': False
                },
                'operation': {
                    'authentication': {
                        'sessionid': self.__session_id
                    },
                    'content': {
                        'function': {
                            '@controlid': str(uuid.uuid4()),
                            key: data[key]
                        }
                    }
                }
            }
        }

        response = self._post_request(dict_body, self.__api_url)
        return response['result']
