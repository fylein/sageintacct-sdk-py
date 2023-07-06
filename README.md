# Sage Intacct SDK
Python SDK to access Sage Intacct web services

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).

        $ pip install sageintacctsdk

## Usage

To use this SDK you'll need these Sage Intacct credentials used for authentication: **sender ID**, **sender password**, **user ID**, **company ID** and **user password**.

This SDK is very easy to use.
1. First you'll need to create a connection using the main class SageIntacctSDK.
```python
from sageintacctsdk import SageIntacctSDK

connection = SageIntacctSDK(
    sender_id='<YOUR SENDER ID>',
    sender_password='<YOUR SENDER PASSWORD>',
    user_id='<YOUR USER ID>',
    company_id='<YOUR COMPANY ID>',
    user_password='<YOUR USER PASSWORD>'
)
```
2. After that you'll be able to access any of the 28 API classes: accounts, ap_payments, ar_invoices, ar_payments, attachments, bills, charge_card_accounts, charge_card_transactions, checking_accounts, classes, contacts, customers, departments, employees, expense_payment_types, expense_reports, expense_types, gl_detail, items, locations, order_entry_transactions, projects, reimbursements, revenue_recognition_schedules, revenue_recognition_schedule_entries, savings_accounts, tasks and vendors.
```python
"""
USAGE: <SageIntacctSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Create a new Expense Report of 3800 USD, spent at 2019-28-11 and from employee with employee id E101
data = {
    'employeeid': 'E101',
    'datecreated': {
        'year': 2019,
        'month': 11,
        'day': 28
    },
    'state': 'Approved',
    'description': 'Team lunch',
    'expenses': {
        'expense': [
            {
                'expensetype': 'Food',
                'amount': 3800,
                'expensedate': {
                    'year': 2019,
                    'month': 11,
                    'day': 28
                }
            }
        ]
    }
}
response = connection.employees.post(data)

# Use get_all methods to get all objects of certain types
response = connection.accounts.get_all()

# Get details of Employee with EMPLOYEEID E101
response = connection.employees.get(field='EMPLOYEEID', value='E101')
```

## Advanced Queries
Several methods of querying the Sage Inacct API exists within the SDK.  <get_by_query> allows you to specify multiple
critera using textual mathematical operators and logical filters.

Arguments are passed to and_filter, or_filter, or both.  The and_filter is the default operator to pass filters to.
For example if you want to pass a single operator without a logical context you would pass it to and_filter.

You must pass multiple operators to or_filter.

You may also format your own filter payload in accordance with API documentation and pass to the function.

See query structures here: https://developer.intacct.com/web-services/queries/

Warning: Operators can only be used once in a given logical context. and_filter cannot accept multiple 'equalto' operators
for example.  This is an API limitation.

```python
#
# Returns Data Structure of object to perform query on.  Helpful to identify field keys.
print(connection.gl_detail.get_lookup())

# Returns records between specified dates
query_tuple_between = [('between','ENTRY_DATE',['01/01/2020','12/31/2020'])]
fields = ['RECORDNO','ENTRY_DATE','BATCH_NO','ACCOUNTNO','DEBITAMOUNT']
response = connection.gl_detail.get_by_query(fields=fields,and_filter=query_tuple_between)

# Returns records between specified accounts
query_tuple_multiple =[('greaterthan','ACOUNTNO','6000'),('lessthan','ACCOUNTNO','7000')]
response = connection.gl_detail.get_by_query(fields=fields,and_filter=query_tuple_multiple)

# Returns records that match list
in_list = ['1000','1100','1200']
query_tuple_in = [('in','ACCOUNTNO',in_list)]
response = connection.gl_detail.get_by_query(fields=fields,and_filter=query_tuple_in)

payload = {'and':{'equalto':{'field':'ACCOUNTNO','value':'1000'}}}
response = connnection.gl_detail.get_by_query(filter_payload=payload)

```

See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
