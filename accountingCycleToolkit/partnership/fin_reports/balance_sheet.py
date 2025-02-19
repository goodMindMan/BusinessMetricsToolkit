import pandas as pd

from partnership.account_types.assets import asset_accounts as asset_lst
from partnership.account_types.liabilities import liability_accounts as lia_lst
from partnership.fin_reports.income_stat import IncomeStatement as income  

import root_account

def make_dict(list:list):

    accounts_dict = {}
    for account in list:
        accounts_dict[account] = 0
    return accounts_dict


class BalanceSheet:
    def __init__(self, all_accounts:list):
        self.all_accounts = all_accounts

        self.asset_accounts = make_dict(asset_lst)
        self.asset_accounts.update({key: 0 for key in ['ttl_current_assets', 'ttl_noncurrent_assets', 'other_assets', 'other_contra_assets', 'ttl_assets']})

        self.liability_accounts = make_dict(lia_lst)
        self.liability_accounts.update({key: 0 for key in ['ttl_current_liabilities', 'ttl_noncurrent_liabilities', 'other_liabilities', 'ttl_liabilities']})

        self.net_income = income.net_income(self.all_accounts)
    
    def assets_prep(self, used_account:root_account.Account):
        
        def add_balance_curr(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_current_assets'] +=used_account.balance()
            self.asset_accounts['ttl_assets'] +=used_account.balance()

        def sub_balance(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_current_assets'] -=used_account.balance()
            self.asset_accounts['ttl_assets'] -=used_account.balance()

        def add_balance_noncurr(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_noncurrent_assets'] +=used_account.balance()
            self.asset_accounts['ttl_assets'] +=used_account.balance()

        if used_account.account_sub_type() == 'cash':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'account_receivables':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'inventory':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'prepaid':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'investments':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'equipments':
            add_balance_noncurr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'land':
            add_balance_noncurr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'intangable_assets':
            add_balance_noncurr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'acc_depreciation':
            sub_balance('acc_depreciation')
        
        elif used_account.account_sub_type() == 'acc_depletion':
            sub_balance('acc_depletion')
        
        elif used_account.account_sub_type() == 'allowance_doubtful':
            sub_balance('allowance_doubtful')

        else:
            if used_account.account_type() == 'Asset':
                self.asset_accounts['othr_assets'] +=used_account.balance()
                self.asset_accounts['ttl_assets'] +=used_account.balance()
            
            elif used_account.account_type() == 'contra_assets':
                sub_balance('other_contra_assets')
            else:   
                print(f'An error occured while incrementing the Asset account:`{used_account.name}`')
    
    def liabilities_prep(self, used_account:root_account.Account):
        
        def add_balance_curr(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_current_liabilities'] +=used_account.balance()
            self.asset_accounts['ttl_liabilities'] +=used_account.balance()

        def sub_balance(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_current_liabilities'] -=used_account.balance()
            self.asset_accounts['ttl_liabilities'] -=used_account.balance()

        def add_balance_noncurr(name:str):
            self.asset_accounts['ttl_' + name] +=used_account.balance()
            self.asset_accounts['ttl_noncurrent_liabilities'] +=used_account.balance()
            self.asset_accounts['ttl_liabilities'] +=used_account.balance()

        if used_account.account_sub_type() == 'account_pay':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'notes_pay':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'salaries_pay':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'interest_pay':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'unearned_revenue':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'cpltd':
            add_balance_curr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'longterm_notes_pay':
            add_balance_noncurr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'loan':
            add_balance_noncurr(used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'contra_liability':
            sub_balance('contra_liability')

        else:
            if used_account.account_type() == 'debt':
                self.liability_accounts['othr_liabilities'] +=used_account.balance()
                self.liability_accounts['ttl_liabilities'] +=used_account.balance()
            
            elif used_account.account_type() == 'contra_liabilities':
                sub_balance('other_contra_liabilities')
            else:   
                print(f'An error occured while incrementing the Liability account:`{used_account.name}`')
