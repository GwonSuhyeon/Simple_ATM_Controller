

from Bank_Server import Bank_Server

from Hardware.cash_bin import CashBin
from Hardware.card_reader import CardReader


class ATM():
    
    def __init__(self):
        self.bank_server = Bank_Server()
        self.cash_bin = CashBin(None, None)
        self.card_reader = CardReader(None)
        self.pin_valid = False
        self.user_id = -1
        self.user_account = None
        self.account_task = ['exit', 'balance check', 'deposit', 'withdraw']
    
    
    def insert_card(self):
        
        ###################################
        
        # For integrate with real bank system.
        
        # self.card_reader.read_card_info()
        
        ###################################
        
        
        # Check the input
        print('Please insert your card (y/n) :', end=' ')
        
        buffer = input()
        if len(buffer) == 0:
            print('ERROR - Wrong input')
            
            return False, None
        
        
        if buffer == 'y' or buffer == 'Y':
            
            return True, buffer
        
        elif buffer == 'N' or buffer == 'n':
            
            return True, buffer
        
        else:
            print('ERROR - Wrong input')
            
            return False, None
    
    
    def input_pin(self):
    
        valid = True
        
        # Check the input
        print('')
        print('Please input your pin number (only number 0~9) :', end=' ')
        
        buffer = input()
        if len(buffer) == 0:
            print('ERROR - Wrong input')
            
            return False
        
        for i in buffer:
            if i < '0' or i > '9':
                print('ERROR - Wrong input')
                
                valid = False
                
                break
        
        if valid == True:
            
            # Request the bank server to validation
            res = self.bank_server.validate_pin(buffer)
            if res == False:
                print('Your pin number validation failed')
                
                return False
            
            self.pin_valid = True
            
            # Get the id of the current user
            res, self.user_id = self.bank_server.get_user_id(buffer)
            if res == False:
                print('Fail to get user id')
                
                return False
        
        return valid
    
    
    def select_account(self):
        
        if self.pin_valid == False:
            print('You need a pin number')
            
            return False
        
        # Look up the user's account list
        res, account = self.bank_server.load_user_account(self.user_id)
        if res == False:
            print('Your account does not exist')
            
            return False
        
        # Show user's account list and select account
        print('')
        for i, a in enumerate(account):
            print(f'{i+1}. {a}')
        print('Please select your account (only list number) :', end=' ')
        
        try:
            buffer = int(input())
            
        except ValueError:
            print('Error - Wrong input')
            
            return False
        
        if buffer < 1 or buffer > len(account):
            print('Error - Wrong input')
            
            return False
        
        self.user_account = account[buffer - 1]
        
        return True
        
    
    def select_account_task(self):
        
        ###################################
        
        # For integrate with real bank system.
        
        # cash_bin_amount = self.cash_bin.check_cash_bin_amount()
        # self.cash_bin.update_cash_bin_amount()
        
        ###################################
        
        
        while True:
            
            # Show account tasks and select task
            print('')
            for i, task in enumerate(self.account_task):
                print(f'{i}. {task}')
            print('Please select the task you want (only list number) :', end=' ')
            
            try:
                buffer = int(input())
                
            except ValueError:
                print('Error - Wrong input')
                
                return False
            
            if buffer < 0 or buffer >= len(self.account_task):
                print('Error - Wrong input')
                
                return False
            
            
            # Check user's account balance
            res, balance = self.bank_server.check_user_balance(self.user_id, self.user_account)
            if res == False:
                print('Fail to check balance')
                
                return False
            
            balance_str = format(balance, ',')
            
            
            # ATM exit
            if buffer == 0:
                break
            
            # Check balance
            elif buffer == 1:
                print('')
                print(f'{self.user_account} current balance : USD{balance_str}')
                
                pass
            
            # Deposit
            elif buffer == 2:
                print('')
                print(f'{self.user_account} current balance : USD{balance_str}')
                print('Please enter the amount to be deposited (only number 0~9) :', end=' ')
                
                try:
                    buffer = int(input())
                    
                except ValueError:
                    print('Error - Wrong input')
                    
                    return False
                
                # Check depositable amount
                if buffer < 1:
                    print('Error - Wrong input')
                    
                    return False
                
                # Deposit user's account balance
                res, new_balance = self.bank_server.deposit_user_balance(self.user_id, self.user_account, buffer)
                if res == False:
                    print('Fail to deposit')
                    
                    return False
                
                new_balance_str = format(new_balance, ',')
                
                print(f'{self.user_account} new balance : USD{new_balance_str}')
            
            # Withdraw
            elif buffer == 3:
                print('')
                print(f'{self.user_account} withdrawable amount : USD{balance_str}')
                print('Please enter the amount to be withdrawn (only number 0~9) :', end=' ')
                
                try:
                    buffer = int(input())
                    
                except ValueError:
                    print('Error - Wrong input')
                    
                    return False
                
                # Check withdrawable amount
                if buffer < 1 or buffer > balance:
                    print('Error - Wrong input')
                    
                    return False
                
                # Withdraw user's account balance
                res, new_balance = self.bank_server.withdraw_user_balance(self.user_id, self.user_account, buffer)
                if res == False:
                    print('Fail to deposit')
                    
                    return False
                
                new_balance_str = format(new_balance, ',')
                
                print(f'{self.user_account} new balance : USD{new_balance_str}')
        
        
        return True