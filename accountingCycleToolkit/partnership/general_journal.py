import pandas as pd
import random

from partnership.root_account import Account

class Journaling:
    general_journal = pd.DataFrame(columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
    used_accounts_names = []
    used_accounts = []
    
    def two_line_entry(self, date:str, dr_acc:Account, cr_acc:Account, amount:float):
        
        accounts =[dr_acc, cr_acc]
        for acc in accounts:
            try:
                acc.account_type()
                if acc not in self.used_accounts:
                    self.used_accounts.append(acc)
                    self.used_accounts_names.append(acc.name)
            except TypeError:
                print(f'{acc} may not be a properly defined account or isn\'t an account at all,\nmake sure to enter an instance of `Root.Account`')
        
        
        dr_acc.transaction(date, amount)
        cr_acc.transaction(date, 0 ,amount)
            
        rand_id = round(100000*(random.random()))

        dr_entry = pd.DataFrame([[rand_id, date, dr_acc.name, dr_acc.pr, amount, 0]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
        
        cr_entry = pd.DataFrame([[rand_id ,date, cr_acc.name, cr_acc.pr, 0, amount]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
        
        entry = pd.concat([dr_entry, cr_entry], ignore_index=True)

        self.general_journal = pd.concat([self.general_journal, entry], ignore_index=True)
    
    def three_line_entry(
            self, date:str, 
            acc01:Account, acc01_blnc, acc01_amount:float,
            acc02:Account, acc02_blnc, acc02_amount:float,
            acc03:Account
            ):
        
        accounts = [acc01, acc02, acc03]
        for acc in accounts:
            try:
                acc.account_type()
                if acc not in self.used_accounts:
                    self.used_accounts.append(acc)
                    self.used_accounts_names.append(acc.name)
            except TypeError:
                print(f'{acc} may not be a properly defined account or isn\'t an account at all,\nmake sure to enter an instance of `Root.Account`')

        if acc01_blnc == acc02_blnc:

            acc03_amount = acc01_amount + acc02_amount

            acc01.transaction(date, acc01_amount)
            acc02.transaction(date, acc02_amount)
            acc03.transaction(date, 0, acc03_amount)

            rand_id = round(100000*(random.random()))

            dr_entry01 = pd.DataFrame([[rand_id, date, acc01.name, acc01.pr, acc01_amount, 0]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
            print(dr_entry01)
            dr_entry02 = pd.DataFrame([[rand_id, date, acc02.name, acc02.pr, acc02_amount, 0]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])

            cr_entry03 = pd.DataFrame([[rand_id,date, acc03.name, acc03.pr, 0, acc03_amount]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
            
            entry = pd.concat([dr_entry01, dr_entry02, cr_entry03], ignore_index=True)

            self.general_journal = pd.concat([self.general_journal, entry], ignore_index=True)
        
        else:
            if (acc01_amount + acc02_amount) != acc03_amount:
                print('INvalid journal entry, debit doesn\'t equal credit')

            acc01.transaction(date, acc01_amount)
            acc02.transaction(date, 0, acc02_amount)
            acc03.transaction(date, 0, acc03_amount)

            rand_id = round(100000*(random.random()))

            dr_entry01 = pd.DataFrame([[rand_id, date, acc01.name, acc01.pr, acc01_amount, 0]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
        
            cr_entry01 = pd.DataFrame([[rand_id, date, acc02.name, acc02.pr, acc02_amount, 0]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])

            cr_entry02 = pd.DataFrame([[rand_id,date, acc03.name, acc03.pr, 0, acc03_amount]]
                        , columns=['id', 'date', 'account_name', 'pr', 'dr', 'cr'])
            
            entry = pd.concat([dr_entry01, cr_entry01, cr_entry02], ignore_index=True)

            self.general_journal = pd.concat([self.general_journal, entry], ignore_index=True)
    
    def all_accounts(self):
        return self.used_accounts
