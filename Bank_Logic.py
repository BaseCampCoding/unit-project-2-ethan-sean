import sqlite3

con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, balance REAL)')

con.commit()


class account:
    def __init__(self):
        self.balance = 0

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw

    def total_balance(self):
        return self.balance
    
def is_login_password_valid(username: str, password: str) -> bool:
    cur.execute('SELECT * FROM users WHERE user_name = ? AND user_password = ?', [username, password])
    if cur.fetchall():
        return True
    else:
        return False

# def valid_number(num):
#     while True:
#         response = input(num)
#         if response.isdigit():
#             response = float(num)
#             if response > 0:
#                 return response
#         print("Please provide a valid number")

def deposits():
    while True:
        user_deposit = float(input("How much are you wanting to deposit: "))
        if user_deposit:
            cur.execute('SELECT balance FROM users WHERE user_name = ? AND user_password = ?', ()
            current_user = account()
            current_user.deposit(user_deposit)
            print(f"Your new balance is ${current_user.balance}")
            break
        else:
            print("Please give valid deposit amount!")     