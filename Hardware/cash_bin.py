

class CashBin:
    
    def __init__(self, cash_bin_id, cash_bin_amount):
        self.cash_bin_id = cash_bin_id
        self.cash_bin_amount = cash_bin_amount
    
    
    def check_cash_bin_amount(self):
        
        return self.cash_bin_amount
    
    
    def update_cash_bin_amount(self, type, update_amount):
        
        if type == 'deposit':
            self.cash_bin_amount += update_amount
        
        elif type == 'withdraw':
            self.cash_bin_amount -= update_amount
        
        return