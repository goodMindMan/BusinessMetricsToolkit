import pandas as pd

# the accounting system should start by defining an abstract Account
# this abstract account:
    #1. has a name an id (pr) 
    #2. has its own ledger that logs transactions that an account is involved in
    #3. is able to log a transaction into the ledger created
class Account:
    def __init__(self, pr:int, name: str):
        self.pr = pr
        self.name = name
        self.ledger = pd.DataFrame(columns=self.columns) #O(mn)
    
    columns  = ['Date', 'Debit', 'Credit'] 
    
    def transaction(self, date: str, dr_amount:float = 0, cr_amount:float = 0): 
        transaction = pd.DataFrame([[date, dr_amount, cr_amount]], columns=self.columns) #O(mn)
        self.ledger = pd.concat([self.ledger, transaction], ignore_index=True) #O(n) time&Space

# The next step is creating subclasses (in `account_types`) that are going to be actually used 
# Each file has it's own mother class that inherets from root and adds three main functionalities:
    #1. An attribute with the `account_type` e.g. asset, revenue, expense, etc...
    #2. An attribute containing a calculation of the balance of the account
    #3. A `show_ledger` method that prints out the ledger for each account after
    # Itconcatenates a balance row that calculates the net amount in the account
        #- The balance row changes based on the account type, it is either debit or credit

# After that we creating suclasses to the mother class of each file in `account_types`
# It only adds an extra attribute with the name of the category of the account stores in it e.g. cash, cogs, payables, etc...
