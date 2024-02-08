

from Data.pin import pin


def validation(user_pin):
    
    if len(user_pin) == 0:
        
        return False
    
    # Check the user's pin number
    if user_pin not in pin:
        
        return False
    
    return True