import pandas as pd

from ..root_account import Account

class Revenue(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'revenue'
        
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = cr_sum - dr_sum 
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class sales(Revenue):  
    def account_type(self):
        return 'sales'

class GainDisposal(Revenue):  
    def account_type(self):
        return 'gain_disposal'
    
class ContraRev(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'contra_revenue'
    
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = dr_sum - cr_sum
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class Discount(ContraRev):      
    def account_type(self):
        return 'discount'

class ReturnsAllowances(ContraRev):
    def account_type(self):
        return 'returns_allowances'

revenue_accounts = [
        'sales', 
        'othr_contra_revenue', 'gain_disposal', 'discount', 'returns_allowances', 
        ]
