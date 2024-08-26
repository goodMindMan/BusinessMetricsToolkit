import pandas as pd

from ..root_account import Account

# We need to create two main classes:
    # `Liability`: Credit Normal balance (handles basic current and non current accounts)
    # `ContraLiability`: Debit Normal balance (handles really rare cases)
class Liability(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Credit'].sum() - self.ledger['Debit'].sum()
        self.account_type = 'debt'

    def show_ledger(self):
        '''
        Credit is the normal balance of `Liability` accounts, that is y the left field is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)

class AccountPayable(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'account_pay'

class NotesPayable(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'notes_pay'

class SalariesPayable(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'salaries_pay'

class InterestPayable(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'interest_pay'    

class UnearnedRevenue(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'unearned_revenue'

class cpltd(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'cpltd'

class LongtermNotesPayable(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'longterm_notes_pay'

class Loan(Liability):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_type = 'loan'

class ContraLiability(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = ['Debit'].sum() - ['Credit'].sum()
        self.account_type = 'contra_liability'
       
        
    def show_ledger(self):
        '''
        Credit is the normal balance of `ContraLiability` accounts, that is y the left field is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)


liability_accounts = [
    'account_pay','notes_pay','salaries_pay','interest_pay','unearned_revenue','cpltd',
    'longterm_notes_pay','loan', 'contra_liability'
]
