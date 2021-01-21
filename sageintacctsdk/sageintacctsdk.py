"""
Sage Intacct Python SDK
"""
from .apis import *

class SageIntacctSDK:
    """
    Sage Intacct SDK
    """

    def __init__(self, sender_id: str, sender_password: str, user_id: str, company_id: str, user_password: str):
        """
        Initialize connection to Sage Intacct
        :param sender_id: Sage Intacct sender id
        :param sender_password: Sage Intacct sener password
        :param user_id: Sage Intacct user id
        :param company_id: Sage Intacct company id
        :param user_password: Sage Intacct user password
        """
        # Initializing variables
        self.__sender_id = sender_id
        self.__sender_password = sender_password
        self.__user_id = user_id
        self.__company_id = company_id
        self.__user_password = user_password

        self.__access_token = None

        self.api_base = ApiBase()
        self.contacts = Contacts()
        self.locations = Locations()
        self.employees = Employees()
        self.accounts = Accounts()
        self.expense_types = ExpenseTypes()
        self.attachments = Attachments()
        self.expense_reports = ExpenseReports()
        self.vendors = Vendors()
        self.bills = Bills()
        self.projects = Projects()
        self.departments = Departments()
        self.charge_card_accounts = ChargeCardAccounts()
        self.charge_card_transactions = ChargeCardTransactions()
        self.customers = Customers()
        self.items = Items()

        self.update_sender_id()
        self.update_sender_password()
        self.update_session_id()

    def update_sender_id(self):
        """
        Update the sender id in all API objects.
        """
        self.api_base.set_sender_id(self.__sender_id)
        self.contacts.set_sender_id(self.__sender_id)
        self.locations.set_sender_id(self.__sender_id)
        self.employees.set_sender_id(self.__sender_id)
        self.accounts.set_sender_id(self.__sender_id)
        self.expense_types.set_sender_id(self.__sender_id)
        self.attachments.set_sender_id(self.__sender_id)
        self.expense_reports.set_sender_id(self.__sender_id)
        self.vendors.set_sender_id(self.__sender_id)
        self.bills.set_sender_id(self.__sender_id)
        self.projects.set_sender_id(self.__sender_id)
        self.departments.set_sender_id(self.__sender_id)
        self.charge_card_accounts.set_sender_id(self.__sender_id)
        self.charge_card_transactions.set_sender_id(self.__sender_id)
        self.customers.set_sender_id(self.__sender_id)
        self.items.set_sender_id(self.__sender_id)

    def update_sender_password(self):
        """
        Update the sender password in all API objects.
        """
        self.api_base.set_sender_password(self.__sender_password)
        self.contacts.set_sender_password(self.__sender_password)
        self.locations.set_sender_password(self.__sender_password)
        self.employees.set_sender_password(self.__sender_password)
        self.accounts.set_sender_password(self.__sender_password)
        self.expense_types.set_sender_password(self.__sender_password)
        self.attachments.set_sender_password(self.__sender_password)
        self.expense_reports.set_sender_password(self.__sender_password)
        self.vendors.set_sender_password(self.__sender_password)
        self.bills.set_sender_password(self.__sender_password)
        self.projects.set_sender_password(self.__sender_password)
        self.departments.set_sender_password(self.__sender_password)
        self.charge_card_accounts.set_sender_password(self.__sender_password)
        self.charge_card_transactions.set_sender_password(self.__sender_password)
        self.customers.set_sender_password(self.__sender_password)
        self.items.set_sender_password(self.__sender_password)

    def update_session_id(self):
        """
        Update the session id and change it in all API objects.
        """
        self.__session_id = self.api_base._get_session_id(self.__user_id, self.__company_id, self.__user_password)
        self.api_base.set_session_id(self.__session_id)
        self.contacts.set_session_id(self.__session_id)
        self.locations.set_session_id(self.__session_id)
        self.employees.set_session_id(self.__session_id)
        self.accounts.set_session_id(self.__session_id)
        self.expense_types.set_session_id(self.__session_id)
        self.attachments.set_session_id(self.__session_id)
        self.expense_reports.set_session_id(self.__session_id)
        self.vendors.set_session_id(self.__session_id)
        self.bills.set_session_id(self.__session_id)
        self.projects.set_session_id(self.__session_id)
        self.departments.set_session_id(self.__session_id)
        self.charge_card_accounts.set_session_id(self.__session_id)
        self.charge_card_transactions.set_session_id(self.__session_id)
        self.customers.set_session_id(self.__session_id)
        self.items.set_session_id(self.__session_id)
