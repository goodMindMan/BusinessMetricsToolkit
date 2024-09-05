
from partnership.root_account import Account as acc
from partnership import general_journal as gj
from partnership.account_types import expenses as exp 
from partnership.account_types import revenue as rev


def make_accs_dict(list:list):
    
    def make_ttl(ttl_str , account):
        return ttl_str + account

    ttl_str = 'ttl_' 
    def make_dict(list):
        accounts_dict = {}
        for account in list:
            accounts_dict[make_ttl(ttl_str, account.account_sub_type)] = 0
        return accounts_dict

    make_dict(list)

def get_rev_used_accs(used_accs):
    rev_used_accs = []
    for accnt in used_accs:
        if 'revenue' == accnt.account_type:
            rev_used_accs.append(accnt)
    return rev_used_accs

def get_exp_used_accs(used_accs):
    exp_used_accs = []
    for accnt in used_accs:
        if 'expense' == accnt.account_type:
            exp_used_accs.append(accnt)
    return exp_used_accs

class Income:

    def summon_exp():
        
        exp_all = [subclass().account_sub_type() for subclass in exp.__subclasses__()]
        return exp_all
    
    def summon_rev():
        
        rev_all = [subclass().account_sub_type() for subclass in rev.__subclasses__()]
        return rev_all

    used_accs = gj.used_accs

    rev_used_accs = get_rev_used_accs(used_accs)

    exp_used_accs = get_exp_used_accs(used_accs)

    rev_used_accs_dicts = make_accs_dict(get_rev_used_accs(used_accs))

    exp_used_accs_dicts = make_accs_dict(get_exp_used_accs(used_accs))

    def rev_calc(self, rev_acc):
    
        if rev_acc.account_sub_type() == 'sales':
            self.rev_accs['ttl_sales'] +=rev_acc.balance()
            self.rev_accs['ttl_rev'] +=rev_acc.balance()

        elif rev_acc.account_sub_type() == 'gain_disposal':
            self.rev_accs['ttl_gain_disposal'] +=rev_acc.balance()
            self.rev_accs['ttl_rev'] +=rev_acc.balance()

        elif rev_acc.account_sub_type() == 'discount':
            self.rev_accs['ttl_discount'] +=rev_acc.balance()
            self.rev_accs['ttl_rev'] -=rev_acc.balance()

        elif rev_acc.account_sub_type() == 'returns_allowances':
            self.rev_accs['ttl_returns_allowances'] +=rev_acc.balance()
            self.rev_accs['ttl_rev'] -=rev_acc.balance()
        
        else:
            if rev_acc.account_type() == 'revenue':
                self.rev_accs['ttl_othr_rev'] +=rev_acc.balance()
                self.rev_accs['ttl_rev'] +=rev_acc.balance()
            
            elif rev_acc.account_type() == 'contra_revenue':
                self.rev_accs['ttl_othr_contra_revenue'] +=rev_acc.balance()
                self.rev_accs['ttl_rev'] -=rev_acc.balance()
            
            else:   
                print(f'An error occured while incrementing the revenue account:`{rev_acc.name}`')

    def exp_calc(self, exp_acc):

        if exp_acc.account_sub_type() == 'cogs':
            self.exp_accs['ttl_cogs'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'salaries':
            self.exp_accs['ttl_salaries'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'rent':
            self.exp_accs['ttl_rent'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'utilities':
            self.exp_accs['ttl_utilities'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'interest':
            self.exp_accs['ttl_interest'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'insurance':
            self.exp_accs['ttl_insurance'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'depreciation':
            self.exp_accs['ttl_depreciation'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'depletion':
            self.exp_accs['ttl_depletion'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        elif exp_acc.account_sub_type() == 'bad_debt':
            self.exp_accs['ttl_bad_debt'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()
        
        elif exp_acc.account_sub_type() == 'loss_disposal':
            self.exp_accs['ttl_loss_disposal'] +=exp_acc.balance()
            self.exp_accs['ttl_exp'] +=exp_acc.balance()

        else:
            if exp_acc.account_type() == 'expense':
                self.exp_accs['ttl_othr_exp'] +=exp_acc.balance()
                self.exp_accs['ttl_exp'] +=exp_acc.balance()
            else:
                print(f'An error occured while incrementing the expense account:`{exp_acc.name}`')

    def income_processing(self):

        
