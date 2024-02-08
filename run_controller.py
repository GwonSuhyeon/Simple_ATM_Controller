

from ATM import ATM


def main():
    
    # ATM object
    atm = ATM()
    if atm is None:
        print('ATM is not working')
        
        return
    
    
    # Implemented to Insert Card
    res, buffer = atm.insert_card()
    if res == False:
        print('Shut down the ATM')
        
        return
    
    if res == True and (buffer == 'N' or buffer == 'n'):
        print('Exit')
        
        return
    
    # Implemented to PIN number
    res = atm.input_pin()
    if res == False:
        print('Shut down the ATM')
        
        return
    
    # Implemented to Select Account
    res = atm.select_account()
    if res == False:
        print('Shut down the ATM')
        
        return
    
    # Implemented to See Balance/Deposit/Withdraw
    res = atm.select_account_task()
    if res == False:
        print('Shut down the ATM')
        
        return
    
    print('Exit')
    
    
    return
    

if __name__ == '__main__':
    
    # Start simple ATM controller
    main()