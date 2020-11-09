import sqlite3
import Bank_Logic
print("Welcome to SaveBetterBank(SBB)")
main_menu = input("""What would you like to do?
    - Login
    - Create an account
    - Delete an existing account
    Type Here: """
)

class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

balance = 0
class account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, deposit):
        self.deposit = self.deposit + balance
    
    def withdraw(self, withdraw):
        if self.balance >= amount:
            self.withdraw - balance
