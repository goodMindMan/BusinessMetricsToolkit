import pandas as pd

from ..root_account import Account

class Expense(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'expense'
       
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = dr_sum - cr_sum
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class Cogs(Expense):
    def account_type(self):
        return 'cogs'
class Salaries(Expense):
    def account_type(self):
        return 'salaries'

class Rent(Expense):
    def account_type(self):
        return 'rent'

class Utilities(Expense):
    def account_type(self):
        return 'utilities'

class Interest(Expense):
    def account_type(self):
        return 'interest'

class Insurance(Expense):
    def account_type(self):
        return 'insurance'

class Depreciation(Expense):
    def account_type(self):
        return 'depreciation'

class Depletion(Expense):
    def account_type(self):
        return 'depletion'

class BadDebt(Expense):
    def account_type(self):
        return 'bad_debt' 

class LossDisposal(Expense):
    def account_type(self):
        return 'loss_disposal'

# Add new sub types here
expense_accounts = [
        'ttl_cogs', 'ttl_salaries', 'ttl_rent', 
        'ttl_utilities', 'ttl_interest', 'ttl_insurance', 'ttl_depreciation', 
        'ttl_depletion', 'ttl_bad_debt', 'ttl_loss_disposal', 
        'ttl_othr_exp', 'ttl_exp' 
]
