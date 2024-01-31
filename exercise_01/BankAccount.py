class BankAccount:
    
    def __init__(self, account_name,balance):
        self.account_name = account_name
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0:
            self.balance = amount + self.balance
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        
    def get_balance(self):
        print(f"{self.account_name}  has a balance of {self.balance}")
        