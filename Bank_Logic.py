import sqlite3

con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, user_id INT)')

cur.execute('CREATE TABLE IF NOT EXISTS accounts(account_id INT, balance REAL, transactions TEXT)')
con.commit()

def compare_userid():
    while True:
        cur.execute('SELECT user_id FROM users INNER JOIN accounts ON user_id = account_id')
        con.commit()
        if cur.fetchall():
            return True
        else: 
            return False

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

def valid_number(num):
    while True:
        response = input(num)
        if response.isdigit():
            response = float(num)
            if response >= 0:
                return response
        print("Please provide a valid number")

def deposit():
    while True:
        user_deposit = input("How much are you wanting to deposit: ")
        if valid_number(user_deposit):
            cur.execute('SELECT balance FROM accounts')
            

            