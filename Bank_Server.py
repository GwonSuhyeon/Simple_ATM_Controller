

from Server_API import account_manage, pin_manage
from Data.user import users


class Bank_Server:
    
    def validate_pin(self, user_pin):
        
        if len(user_pin) == 0:
            
            return False
        
        # Call the validation api
        res = pin_manage.validation(user_pin)
        if res == False:
            
            return False
        
        return True
    
    
    def get_user_id(self, user_pin):
        
        user_id = -1
        
        if len(user_pin) == 0:
            
            return False, user_id
        
        # Find user's pin number
        for i, user in enumerate(users.values()):
            if user.pin == user_pin:
                user_id = i
                
                break
        
        return True, user_id
    
    
    def load_user_account(self, user_id):
        
        # Call the load account api
        res, user_account = account_manage.load_account(user_id)
        if res == False:
            
            return False, None
        
        return res, user_account
    
    
    def check_user_balance(self, user_id, user_account):
        
        # Call the check balance api
        res, balance = account_manage.check_balance(user_id, user_account)
        if res == False:
            
            return False, None
        
        return res, balance
    
    
    def deposit_user_balance(self, user_id, user_account, deposit_amount):
        
        # Call the deposit balance api
        res, new_balance = account_manage.deposit_balance(user_id, user_account, deposit_amount)
        if res == False:
            
            return False, None
        
        return res, new_balance
    
    
    def withdraw_user_balance(self, user_id, user_account, withdraw_amount):
        
        # Call the withdraw balance api
        res, new_balance = account_manage.withdraw_balance(user_id, user_account, withdraw_amount)
        if res == False:
            
            return False, None
        
        return res, new_balance