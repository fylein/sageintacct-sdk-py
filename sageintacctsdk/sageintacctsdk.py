"""
Sage Intacct Python SDK
"""
from .apis import ApiBase, Contacts, Locations, Employees, Accounts, ExpenseTypes, Attachments, ExpenseReports,\
    Vendors, Bills, Projects, Departments, ChargeCardAccounts, ChargeCardTransactions, Customers, Items,\
    APPayments, Reimbursements, CheckingAccounts, SavingsAccounts, Tasks, ExpensePaymentTypes, Dimensions,\
    DimensionValues, LocationEntities, ARInvoices, TaxDetails, GLDetail, Classes, JournalEntries,\
    RevRecSchedules, RevRecScheduleEntries, CostTypes, OrderEntryTransactions


class SageIntacctSDK:
    """
    Sage Intacct SDK
    """

    def __init__(self, sender_id: str, sender_password: str, user_id: str,
        company_id: str, user_password: str, entity_id: str=None):
        """
        Initialize connection to Sage Intacct
        :param sender_id: Sage Intacct sender id
        :param sender_password: Sage Intacct sener password
        :param user_id: Sage Intacct user id
        :param company_id: Sage Intacct company id
        :param user_password: Sage Intacct user password
        :param (optional) entity_id: Sage Intacct entity ID
        """
        # Initializing variables
        self.__sender_id = sender_id
        self.__sender_password = sender_password
        self.__user_id = user_id
        self.__company_id = company_id
        self.__user_password = user_password
        self.__entity_id = entity_id

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
        self.ap_payments = APPayments()
        self.ar_invoices = ARInvoices()
        self.reimbursements = Reimbursements()
        self.checking_accounts = CheckingAccounts()
        self.savings_accounts = SavingsAccounts()
        self.dimensions = Dimensions()
        self.dimension_values = DimensionValues()
        self.tasks = Tasks()
        self.expense_payment_types = ExpensePaymentTypes()
        self.location_entities = LocationEntities()
        self.tax_details = TaxDetails()
        self.gl_detail = GLDetail()
        self.classes = Classes()
        self.journal_entries = JournalEntries()
        self.rev_rec_schedules = RevRecSchedules()
        self.rev_rec_schedule_entries = RevRecScheduleEntries()
        self.cost_types = CostTypes()
        self.order_entry_transactions = OrderEntryTransactions()
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
        self.ap_payments.set_sender_id(self.__sender_id)
        self.ar_invoices.set_sender_id(self.__sender_id)
        self.reimbursements.set_sender_id(self.__sender_id)
        self.checking_accounts.set_sender_id(self.__sender_id)
        self.savings_accounts.set_sender_id(self.__sender_id)
        self.dimensions.set_sender_id(self.__sender_id)
        self.dimension_values.set_sender_id(self.__sender_id)
        self.tasks.set_sender_id(self.__sender_id)
        self.expense_payment_types.set_sender_id(self.__sender_id)
        self.location_entities.set_sender_id(self.__sender_id)
        self.tax_details.set_sender_id(self.__sender_id)
        self.gl_detail.set_sender_id(self.__sender_id)
        self.classes.set_sender_id(self.__sender_id)
        self.journal_entries.set_sender_id(self.__sender_id)
        self.rev_rec_schedules.set_sender_id(self.__sender_id)
        self.rev_rec_schedule_entries.set_sender_id(self.__sender_id)
        self.cost_types.set_sender_id(self.__sender_id)
        self.order_entry_transactions.set_sender_id(self.__sender_id)

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
        self.ap_payments.set_sender_password(self.__sender_password)
        self.ar_invoices.set_sender_password(self.__sender_password)
        self.reimbursements.set_sender_password(self.__sender_password)
        self.checking_accounts.set_sender_password(self.__sender_password)
        self.savings_accounts.set_sender_password(self.__sender_password)
        self.dimensions.set_sender_password(self.__sender_password)
        self.dimension_values.set_sender_password(self.__sender_password)
        self.tasks.set_sender_password(self.__sender_password)
        self.expense_payment_types.set_sender_password(self.__sender_password)
        self.location_entities.set_sender_password(self.__sender_password)
        self.tax_details.set_sender_password(self.__sender_password)
        self.gl_detail.set_sender_password(self.__sender_password)
        self.classes.set_sender_password(self.__sender_password)
        self.journal_entries.set_sender_password(self.__sender_password)
        self.rev_rec_schedules.set_sender_password(self.__sender_password)
        self.rev_rec_schedule_entries.set_sender_password(self.__sender_password)
        self.cost_types.set_sender_password(self.__sender_password)
        self.order_entry_transactions.set_sender_password(self.__sender_password)

    def update_session_id(self):
        """
        Update the session id and change it in all API objects.
        """
        self.__session_id = self.api_base.get_session_id(
        self.__user_id, self.__company_id, self.__user_password, self.__entity_id)
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
        self.ap_payments.set_session_id(self.__session_id)
        self.ar_invoices.set_session_id(self.__session_id)
        self.reimbursements.set_session_id(self.__session_id)
        self.checking_accounts.set_session_id(self.__session_id)
        self.savings_accounts.set_session_id(self.__session_id)
        self.dimensions.set_session_id(self.__session_id)
        self.dimension_values.set_session_id(self.__session_id)
        self.tasks.set_session_id(self.__session_id)
        self.expense_payment_types.set_session_id(self.__session_id)
        self.location_entities.set_session_id(self.__session_id)
        self.tax_details.set_session_id(self.__session_id)
        self.gl_detail.set_session_id(self.__session_id)
        self.classes.set_session_id(self.__session_id)
        self.journal_entries.set_session_id(self.__session_id)
        self.rev_rec_schedules.set_session_id(self.__session_id)
        self.rev_rec_schedule_entries.set_session_id(self.__session_id)
        self.cost_types.set_session_id(self.__session_id)
        self.order_entry_transactions.set_session_id(self.__session_id)
