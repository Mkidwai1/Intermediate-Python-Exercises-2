from BankAccount import BankAccount

my_account = BankAccount("John's Account", 1000)

my_account.deposit(500)

my_account.withdraw(200)

print(my_account.get_balance())  
