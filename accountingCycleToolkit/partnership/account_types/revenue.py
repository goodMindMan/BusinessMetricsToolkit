import pandas as pd

from ..root_account import Account

class Revenue(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Credit'].sum() - self.ledger['Debit'].sum()
        self.account_type = 'revenue'

    def show_ledger(self):
        '''
        Credit is the normal balance of `Revenue` accounts, that is y the left field is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)

class sales(Revenue):  
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'sales'

class GainDisposal(Revenue):  
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'gain_disposal'

print('i now know revenue')
class ContraRev(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = ['Debit'].sum() - ['Credit'].sum()
        self.account_type = 'contra_revenue'
    
    def show_ledger(self): #O(mn)
        '''
        Debit is the normal balance of ContraRev accounts, that is y the right feild is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)

print('i now know contra revenue')
class Discount(ContraRev):      
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'discount'

class ReturnsAllowances(ContraRev):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'returns_allowances'

revenue_accounts = [
        'sales', 
        'othr_contra_revenue', 'gain_disposal', 'discount', 'returns_allowances', 
        ]
