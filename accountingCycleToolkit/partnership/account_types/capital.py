import pandas as pd

from ..root_account import Account #Summons the abstract account

class Equity(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Credit'].sum() - self.ledger['Debit'].sum()
        self.account_type = 'equity'
    
    def show_ledger(self):
        '''
        Credit is the normal balance of Equity accounts, that is y the left feild is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''       
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class Withdrawals(Equity):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Debit'].sum() - self.ledger['Credit'].sum()
        self.account_type = 'withdrawal'

    def show_ledger(self):
        '''
        Debit is the normal balance of Withdrawal accounts, that is y the right feild is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)
