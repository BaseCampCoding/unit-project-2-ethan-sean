import sqlite3

con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, balance REAL)')

con.commit()


class account:
    def user(self, username):
        self.username = cur.execute('SELECT * From users WHERE user_name = ?,'[username])
    def __init__(self):
        cur.execute('SELECT balance FROM users')
        balance = cur.fetchall()
        self.balance = float(balance[0][0])

    def deposit(self, deposit):
        cur.execute('SELECT balance FROM users')
        self.balance = self.balance + deposit
        cur.execute('INSERT INTO users(balance)VALUES(?)'(self.balance))
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

def view_balance(username):
    cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
    balance = cur.fetchall()
    return print(f'Your Balance is currently ${balance[0][0]}')


def deposits(username):
    while True:
        user_deposit = float(input("How much are you wanting to deposit: $"))
        if user_deposit:
            cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
            current_user = account()
            current_user.deposit(user_deposit)
            cur.execute('UPDATE users SET balance = ? WHERE user_name = ?', (user_deposit, username))
            print(f"Your new balance is ${current_user.balance}")
            break
        else:
            print("Please give valid deposit amount!")

def widthdrawls(username):
    while True:
        user_widthdrawls = input("How much are you wanting to withdraw: ")
        if  user_widthdrawls:
            cur.execute('SELECT balance FROM users WHERE user_name = ?', (username))
            current_user = account()
            current_user.withdraw(user_widthdrawls)
            print(f"Your new balance is ${current_user.balance}")
            break
        else:
            print("Please give valid deposit amount!")   