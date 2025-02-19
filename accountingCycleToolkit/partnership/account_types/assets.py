import pandas as pd

from ..root_account import Account #Summons the abstract account

# Programatically there is no difference in functionality and-
# structure between a current and a non-current asset-
# so we only need to create two main classes:
    # `Assets`: debit Normal balance (handles basic current and non current accounts)
    # `ContraAssets`: credit Normal balance (handles accumulated non-cash accounts)
class Asset(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Debit'].sum() - self.ledger['Credit'].sum() 
        self.account_type = 'asset'
    
    def show_ledger(self): #O(mn)
        '''
        Debit is the normal balance of Assets accounts, that is y the right field is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', self.balance, '-']], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)
print('i now know assets')
class Cash(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'cash'

class AccountReceivables(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'account_receivables'

class Inventory(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'inventory'

class PrepaidExpense(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'prepaid'

class ROU(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'rou'

class NotesReceivable(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'notes_receivable'

class Investments(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'investments'

class Equipment(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'equipments'  

class Land(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'land'

class OtherPPE(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'other_ppe'
         
class IntangableAssets(Asset):
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance ,account_type)
        self.account_sub_type = 'intangable_assets'

class ContraAsset(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
        self.balance = self.ledger['Credit'].sum() - self.ledger['Debit'].sum()
        self.account_type = 'contra_asset'

    def show_ledger(self):
        '''
        Credit is the normal balance of `ContraAsset` accounts, that is y the left field is empty i.e. `'-'`
        Space and Time complexity of O(mn) in this case 3*3
        '''
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns) #O(mn)
        return pd.concat([self.ledger, balance_row], ignore_index=True) #O(n)

print('i now know contra assets')
class AccDepreciation(ContraAsset): 
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance, account_type)
        self.account_sub_type = 'acc_depreciation'

class AccDepletion(ContraAsset):   
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance, account_type)
        self.account_sub_type = 'acc_depletion'

class AllowanceDoubtful(ContraAsset):   
    def __init__(self, pr:int, name:str, balance:float, account_type:str):
        super().__init__(pr, name, balance, account_type)   
        self.account_sub_type = 'allowance_doubtful'

# Add new sub types here
asset_accounts = ['ttl_cash', 'ttl_account_receivables', 'ttl_inventory', 'ttl_prepaid', 
        'ttl_notes_receivable', 'ttl_rou',
        'ttl_investments', 'ttl_equipments', 'ttl_land', 'ttl_intangable_assets', 
        'ttl_acc_depreciation', 'ttl_acc_depletion', 'ttl_allowance_doubtful']
