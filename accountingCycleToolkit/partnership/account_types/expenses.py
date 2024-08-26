import pandas as pd

from ..root_account import Account

class Expense(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = ['Debit'].sum() - ['Credit'].sum()
        self.account_type = 'expense'
    
    def show_ledger(self): #O(mn)
        '''
        Debit is the normal balance of Expense accounts, that is y the right feild is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)

class Cogs(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'cogs'

class Salaries(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'salaries'

class Rent(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'rent'

class Utilities(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'utilities'

class Interest(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'interest'

class Insurance(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'insurance'

class Depreciation(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'depreciation'

class Depletion(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'depletion'

class BadDebt(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'bad_debt' 

class LossDisposal(Expense):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'loss_disposal'

# Add new sub types here
expense_accounts = [
        'ttl_cogs', 'ttl_salaries', 'ttl_rent', 
        'ttl_utilities', 'ttl_interest', 'ttl_insurance', 'ttl_depreciation', 
        'ttl_depletion', 'ttl_bad_debt', 'ttl_loss_disposal', 
        'ttl_othr_exp', 'ttl_exp' 
]
