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
2. After that you'll be able to access any of the 22 API classes: accounts, ap_payments, ar_invoices, attachments, bills, charge_card_accounts, charge_card_transactions, checking_accounts, contacts, customers, departments, employees, expense_payment_types, expense_reports, expense_types, items, locations, projects, reimbursements, savings_accounts, tasks,gl_detail and vendors.
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

Several methods of querying the Sage Inacct API exists within the SDK.  Get_by_query allows you to specify multiple 
critera using textual operators and booleans.  
   
Arguments are passed to and_filter, or_filter, or both. 

See query structures here: https://developer.intacct.com/web-services/queries/

Warnings:
1.) The API is rate limited at 2000 records.

2.) Operators can only be used once in a given boolean context. A filter cannot accept multiple 'equalto' operators
for example.

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






```

See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
