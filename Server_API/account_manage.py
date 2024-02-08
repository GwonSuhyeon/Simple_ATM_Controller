

from Data.user import users


# API functions that task related to account


def load_account(user_id):
    
    if user_id < 0:
        
        return False, None
    
    # Find user
    user = users[user_id]
    if user is None:
        
        return False, None
    
    # Get user's account list
    account = list(user.account.keys())
    if len(account) == 0:
        
        return False, None

    return True, account


def check_balance(user_id, user_account):
    
    if user_id < 0 or len(user_account) == 0:
        
        return False, None
    
    # Find user
    user = users[user_id]
    if user is None:
        
        return False, None
    
    # Get balance of the user's account
    balance = user.account[user_account]
    if balance is None:
        
        return False, None
    
    return True, balance


def deposit_balance(user_id, user_account, deposit_amount):
    
    if user_id < 0 or len(user_account) == 0 or deposit_amount < 1:
        
        return False, None
    
    # Find user
    user = users[user_id]
    if user is None:
        
        return False, None
    
    # Update balance of the user's account
    user.account[user_account] += deposit_amount
    
    # Get the updated balance
    new_balance = user.account[user_account]
    if new_balance is None:
        
        return False, None
    
    return True, new_balance


def withdraw_balance(user_id, user_account, withdraw_amount):
    
    if user_id < 0 or len(user_account) == 0 or withdraw_amount < 1:
        
        return False, None
    
    # Find user
    user = users[user_id]
    if user is None:
        
        return False, None
    
    # Update balance of the user's account
    user.account[user_account] -= withdraw_amount
    
    # Get the updated balance
    new_balance = user.account[user_account]
    if new_balance is None:
        
        return False, None
    
    return True, new_balance