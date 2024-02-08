

class User:
    
    def __init__(self, pin, account):
        self.pin = pin
        self.account = account


users = {0: User('12345', {'100-1234-56789': 2024, '100-2233-99999': 30000}), 1: User('10101', {'100-5678-88899': 750}), 2: User('33333', {})}