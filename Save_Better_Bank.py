import sqlite3
import Bank_Logic
print("Welcome to SaveBetterBank(SBB)")
main_menu = input("""What would you like to do?
    - Login
    - Create an account
    - Delete an existing account
    Type Here: """

class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class account:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance
    
    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance - withdraw
    
    def total_balance(self):
        return self.balance

# user = account()
# user1 = user.withdraw(10)
# print(f'Your balance is ${user.balance:.2f}')