import sqlite3
from os import system, name
from time import sleep
import stdiomask
con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, balance REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS info(status TEXT, transactions REAL)')
con.commit()


class account:
    # def user(self, username):
    #     self.username = cur.execute('SELECT * From users WHERE user_name = ?,'[username])
    def __init__(self):
        # cur.execute('SELECT balance FROM users')
        # balance = cur.fetchall()
        # self.balance = float(balance[0][0])
        self.balance = float(0)

    def deposit(self, username, deposit):
        cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
        self.balance = cur.fetchall()
        self.balance = float(self.balance[0][0])
        self.balance = self.balance + deposit
        cur.execute('UPDATE users SET balance = ? WHERE user_name = ?', (self.balance, username))
        con.commit()
        return self.balance

    def withdraw(self, username, withdraw):
        cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
        self.balance = cur.fetchall()
        self.balance = float(self.balance[0][0])
        if self.balance >= withdraw:
            self.balance -= withdraw
            cur.execute('UPDATE users SET balance = ? WHERE user_name = ?', (self.balance, username))
            return self.balance
        print("You don't have enough funds to withdraw this amount")

    def view_balance(self, username):
        cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
        self.balance = cur.fetchall()
        return print(f'Your Balance is currently ${self.balance[0][0]}')

def is_login_password_valid(username: str, password: str) -> bool:
    cur.execute('SELECT * FROM users WHERE user_name = ? AND user_password = ?', [username, password])
    if cur.fetchall():
        return True
    else:
        return False



def deposits(username):
    while True:
        user_deposit = float(input("How much are you wanting to deposit: $"))
        deposit = 'Deposit'
        cur.execute('INSERT INTO info VALUES(?,?)', [deposit, user_deposit])
        if user_deposit:
            current_user = account()
            current_user.deposit(username, user_deposit)
            print(f"Your new balance is ${current_user.balance}")
            break
        else:
            print("Please give valid deposit amount!")

def withdrawls(username):
    while True:
        user_widthdrawls = float(input("How much are you wanting to withdraw: $"))
        withdraw = 'withdrew'
        cur.execute('INSERT INTO info VALUES(?, ?)', [withdraw, user_widthdrawls])
        if user_widthdrawls:
            current_user = account()
            current_user.withdraw(username, user_widthdrawls)
            print(f"Your new balance is ${current_user.balance}")
            break
        else:
            print("Please give valid deposit amount!")   

def remove_account():
    while True:
        print(f'Please Login with the account you would like to delete:')
        login = input('UserName: ') 
        password = stdiomask.getpass(prompt = "Password: ")
        valid_user = is_login_password_valid(login, password)
        if valid_user:
            confirmation = input('''
            Are you sure you want to delete your account? 
            This will permanently delete everything.
            If sure Type (Y/N):  ''').lower()
            if confirmation == "y":
                cur.execute('DELETE FROM users WHERE user_name = ? AND user_password = ?', [login, password])
                print('Successfully Deleted!')
                break
            elif confirmation == "n":
                break
            else:
                ("Provide A Valid Action(a, b, c, etc.)")
        else: 
            print("Please Provide A Valid Login and Password!")

def clear():
    if name == 'nt':
        _ = system('cls')
    

    


def transactions():
    cur.execute('SELECT status, transactions FROM info')
    for info in cur.fetchall():
        print(info[0], info[1])
