import pandas as pd

from ..root_account import Account

class Asset(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'asset'
    
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = dr_sum - cr_sum
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class Cash(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'cash'

class AccountReceivables(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'account_receivables'

class Inventory(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'inventory'

class PrepaidExpense(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'prepaid'

class NotesReceivable(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'notes_receivable'

class Investments(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'investments'

class Equipment(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'equipments'  

class Land(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'land'
    
class IntangableAssets(Asset):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_sub_type(self):
        return 'intangable_assets'

class ContraAsset(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'contra_asset'
     
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = cr_sum - dr_sum 
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class AccDepreciation(ContraAsset):
    def account_sub_type(self):
        return 'acc_depreciation'

class AccDepletion(ContraAsset):
    def account_sub_type(self):
        return 'acc_depletion'

class AllowanceDoubtful(ContraAsset):
    def account_sub_type(self):
        return 'allowance_doubtful'

# Add new sub types here
asset_accounts = ['cash', 'account_receivables', 'inventory', 'prepaid', 'notes_receivable',
        'investments', 'equipments', 'land', 'intangable_assets', 
        'acc_depreciation', 'acc_depletion', 'allowance_doubtful']
