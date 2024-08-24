import pandas as pd

import partnership.root_account as root_account
from partnership.account_types.expenses import expense_accounts as exp_lst
from partnership.account_types.revenue import revenue_accounts as rev_lst
from ..general_journal import Journaling as jour

def import_accounts_todict(list:list):
    
    def make_ttl(ttl_str , account):
        return ttl_str + account

    ttl_str = 'ttl_' 
    def make_dict(list):
        accounts_dict = {}
        for account in list:
            accounts_dict[make_ttl(ttl_str, account)] = 0
        return accounts_dict

    make_dict(list)


class IncomeStatement:
    def __init__(self, all_accounts:list):
        self.all_accounts = all_accounts

        self.revenue_accounts = import_accounts_todict(rev_lst)
        self.revenue_accounts.update({key: 0 for key in ['other_revenue', 'ttl_revenue']})

        self.expenses_accounts = import_accounts_todict(exp_lst)
        self.expenses_accounts.update({key: 0 for key in ['other_expenses', 'ttl_expenses']})   

    def revenue_prep(self, used_account:root_account.Account):
        
        if used_account.account_sub_type() == 'sales':
            self.revenue_accounts['ttl_sales'] +=used_account.balance()
            self.revenue_accounts['ttl_rev'] +=used_account.balance()

        elif used_account.account_sub_type() == 'gain_disposal':
            self.revenue_accounts['ttl_gain_disposal'] +=used_account.balance()
            self.revenue_accounts['ttl_rev'] +=used_account.balance()

        elif used_account.account_sub_type() == 'discount':
            self.revenue_accounts['ttl_discount'] +=used_account.balance()
            self.revenue_accounts['ttl_rev'] -=used_account.balance()

        elif used_account.account_sub_type() == 'returns_allowances':
            self.revenue_accounts['ttl_returns_allowances'] +=used_account.balance()
            self.revenue_accounts['ttl_rev'] -=used_account.balance()
        
        else:
            if used_account.account_type() == 'revenue':
                self.revenue_accounts['ttl_othr_rev'] +=used_account.balance()
                self.revenue_accounts['ttl_rev'] +=used_account.balance()
            
            elif used_account.account_type() == 'contra_revenue':
                self.revenue_accounts['ttl_othr_contra_revenue'] +=used_account.balance()
                self.revenue_accounts['ttl_rev'] -=used_account.balance()
            
            else:   
                print(f'An error occured while incrementing the revenue account:`{used_account.name}`')

    
    def expense_prep(self, used_account:root_account.Account):

        if used_account.account_sub_type() == 'cogs':
            self.expenses_accounts['ttl_cogs'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'salaries':
            self.expenses_accounts['ttl_salaries'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'rent':
            self.expenses_accounts['ttl_rent'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'utilities':
            self.expenses_accounts['ttl_utilities'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'interest':
            self.expenses_accounts['ttl_interest'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'insurance':
            self.expenses_accounts['ttl_insurance'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'depreciation':
            self.expenses_accounts['ttl_depreciation'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'depletion':
            self.expenses_accounts['ttl_depletion'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'bad_debt':
            self.expenses_accounts['ttl_bad_debt'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()
        
        elif used_account.account_sub_type() == 'loss_disposal':
            self.expenses_accounts['ttl_loss_disposal'] +=used_account.balance()
            self.expenses_accounts['ttl_exp'] +=used_account.balance()

        else:
            if used_account.account_type() == 'expense':
                self.expenses_accounts['ttl_othr_exp'] +=used_account.balance()
                self.expenses_accounts['ttl_exp'] +=used_account.balance()
            else:
                print(f'An error occured while incrementing the expense account:`{used_account.name}`')
        
 
    def income_data_processing(self, all_accounts:list):
        
        for used_account in all_accounts:
            try:
                if used_account.account_type() not in ['revenue', 'contra_revenue', 'expense']:
                    
                    print(f"""
                        Account:`{used_account.name}` is an Asset or Liability account,\n 
                        make sure only instances of the following classes or there subclasses are entered:\n
                        'Revenue', 'Expense'
                        """) 
                
                elif used_account.account_type() in [
                    'revenue', 'contra_revenue'
                    ]:
                    self.revenue_prep(used_account)
                
                elif used_account.account_type() == 'expense':
                    self.expense_prep(used_account)
            except (ValueError, TypeError, NameError):
                print('Fault, contact admin')

        exp_acc_keys = [
            'ttl_cogs', 'ttl_salaries', 'ttl_rent', 'ttl_utilities', 'ttl_interest', 'ttl_insurance', 'ttl_depreciation', 
                        'ttl_depletion', 'ttl_bad_debt', 'ttl_loss_disposal', 'ttl_othr_exp'
        ]
        used_exp_acc = self.expenses_accounts
        for acc in exp_acc_keys:
            if 0 == self.rev_acc[acc]:
                used_exp_acc.pop(acc)
        
        rev_acc_keys = ['ttl_sales', 'ttl_othr_contra_revenue', 'ttl_gain_disposal', 'ttl_discount', 'ttl_returns_allowances', 'ttl_othr_rev']
        used_rev_acc = self.revenue_accounts
        for acc in rev_acc_keys:
            if 0 == self.rev_acc[acc]:
                used_rev_acc.pop(acc)
        
        income_dict = used_exp_acc.update(used_rev_acc)
        net_income = income_dict['ttl_rev'] - income_dict['ttl_exp']
        income_dict.update({'net_income': net_income})
        income_statement = pd.DataFrame(list(income_dict.items()), columns=['Account Name', 'Amount'])
        return income_statement, net_income, income_dict['ttl_rev'], income_dict['ttl_exp']
    
    def show_income_stat(self, all_accounts:list):
        income_statement= self.income_data_processing(jour.all_accounts(all_accounts))[1]
        return income_statement

    def net_income(self, all_accounts:list):
        net_income = self.income_data_processing(jour.all_accounts(all_accounts))[2]
        return net_income
    
    def total_reveune(self, all_accounts:list):
        total_reveune = self.income_data_processing(jour.all_accounts(all_accounts))[3]
        return total_reveune
    
    def total_expenses(self, all_accounts:list):
        total_expenses = self.income_data_processing(jour.all_accounts(all_accounts))[4]
        return total_expenses
