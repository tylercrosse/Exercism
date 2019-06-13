import threading

class BankAccount(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        if self.is_open:
            return self.balance
        else:
            raise ValueError('Can not get balance of closed account.')

    def open(self):
        if not self.is_open:
            self.is_open = True
        else:
            raise ValueError('Bank account is already open.')

    def deposit(self, amount):
        if self.is_open:
            if amount > 0:
                self.lock.acquire()
                try:
                    self.balance += amount
                finally:
                    self.lock.release()
            else:
                raise ValueError('Deposit must be positive.')    
        else:
            raise ValueError('Bank acccount needs to be open to make a deposit.')

    def withdraw(self, amount):
        if self.is_open:
            if self.balance - amount >= 0 and amount > 0:
                self.lock.acquire()
                try:
                    self.balance -= amount
                finally:
                    self.lock.release()
            else:
                raise ValueError('Can not withdraw more than balance.')
        else:
            raise ValueError('Bank acccount needs to be open to make a withdrawl.')

    def close(self):
        if self.is_open:
            self.is_open = False
            self.balance = 0
        else: 
            raise ValueError('Bank account is already closed.')
