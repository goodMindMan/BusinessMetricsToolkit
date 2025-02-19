import pandas as pd
    
import partnership.root_account as root_account
from partnership.account_types.expenses import expense_accounts as exp_lst
from partnership.account_types.revenue import revenue_accounts as rev_lst
from ..general_journal import Journaling as jour

print('sucessful imports')

def make_dict(list:list):

    accounts_dict = {}
    for account in list:
        accounts_dict[account] = 0
    return accounts_dict

class IncomeStatement:
    def __init__(self, all_accounts:list):
        self.all_accounts = all_accounts

        self.revenue_accounts = make_dict(rev_lst)
        self.revenue_accounts.update({key: 0 for key in ['other_revenue', 'ttl_rev']})

        self.expense_accounts = make_dict(exp_lst)
        self.expense_accounts.update({key: 0 for key in ['other_expenses', 'ttl_exp']})   
    
    def rev_aggrgt_add(self, account, acc_sub_type):
        self.revenue_accounts['ttl_'+ acc_sub_type] +=account.balance()
        self.revenue_accounts['ttl_rev'] +=account.balance()

    def rev_aggrgt_sub(self, account, acc_sub_type):
        self.revenue_accounts['ttl_'+ acc_sub_type] +=account.balance()
        self.revenue_accounts['ttl_rev'] -=account.balance()
     
    def exp_aggrgt(self, account, acc_sub_type):
        self.expense_accounts['ttl_'+ acc_sub_type] +=account.balance()
        self.expense_accounts['ttl_exp'] +=account.balance()

    def revenue_prep(self, used_account:root_account.Account):
        
        if used_account.account_sub_type() == 'sales':
            self.aggrgt_add(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'gain_disposal':
            self.aggrgt_add(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'discount':
            self.aggrgt_sub(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'returns_allowances':
            self.aggrgt_sub(used_account, used_account.account_sub_type())
        
        else:
            if used_account.account_type() == 'revenue':
                self.aggrgt_add(used_account, used_account.account_sub_type())
            
            elif used_account.account_type() == 'contra_revenue':
                self.aggrgt_sub(used_account, used_account.account_sub_type())
            
            else:   
                print(f'An error occured while incrementing the revenue account:`{used_account.name}`')

    
    def expense_prep(self, used_account:root_account.Account):

        if used_account.account_sub_type() == 'cost_rev':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'salaries':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'rent':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'utilities':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'interest':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'insurance':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'depreciation':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'depletion':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        elif used_account.account_sub_type() == 'bad_debt':
            self.exp_aggrgt(used_account, used_account.account_sub_type())
        
        elif used_account.account_sub_type() == 'loss_disposal':
            self.exp_aggrgt(used_account, used_account.account_sub_type())

        else:
            if used_account.account_type() == 'expense':
                self.exp_aggrgt(used_account, used_account.account_sub_type())

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

        used_exp_acc = self.expense_accounts
        for acc in self.expense_accounts:
            if 0 == self.expense_accounts[acc]:
                used_exp_acc.pop(acc)
        
        used_rev_acc = self.revenue_accounts
        for acc in self.revenue_accounts:
            if 0 == self.revenue_accounts[acc]:
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

print('i now know inom statements')