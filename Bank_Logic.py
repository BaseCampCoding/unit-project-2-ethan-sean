import sqlite3
from os import system, name
from time import sleep
import stdiomask
con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, balance REAL, savings REAL)')

cur.execute('CREATE TABLE IF NOT EXISTS info(user_name TEXT, status TEXT, transactions REAL)')
con.commit()


class account:
    # def user(self, username):
    #     self.username = cur.execute('SELECT * From users WHERE user_name = ?,'[username])
    def __init__(self):
        # cur.execute('SELECT balance FROM users')
        # balance = cur.fetchall()
        # self.balance = float(balance[0][0])
        self.balance = float(0)
        self.saving = float(0)

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
            con.commit()
            return self.balance
        print("You don't have enough funds to withdraw this amount")
    
    def savings(self, username, savings):
        cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
        self.balance = cur.fetchall()
        self.balance = float(self.balance[0][0])
        if self.balance >= savings:
            self.balance -= savings
            self.saving = self.saving + self.balance
            cur.execute('UPDATE users SET balance = ? WHERE user_name = ?', (self.balance, username))
            cur.execute('UPDATE users SET savings = ? WHERE user_name = ?', (self.balance, username))
            con.commit()
            return self.savings
        print("You don't have enough funds to withdraw this amount")

    def view_balance(self, username):
        cur.execute('SELECT balance FROM users WHERE user_name = ?', [username])
        self.balance = cur.fetchall()
        return print(f'Your Balance is currently ${self.balance[0][0]:.2f}')

def is_login_password_valid(username: str, password: str) -> bool:
    cur.execute('SELECT * FROM users WHERE user_name = ? AND user_password = ?', [username, password])
    if cur.fetchall():
        return True
    else:
        return False


def input_number(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isdigit():
            response = float(response)
            if response >= 0:
                return response
        print("Please use a number greater than zero")

def deposits(username):
    while True:
        user_deposit =  input("How much are you wanting to deposit: $")
        if user_deposit.isdigit():
            user_deposit = float(user_deposit)
            deposit = 'Deposit'
            cur.execute('INSERT INTO info VALUES(?, ?, ?)', [username, deposit, user_deposit])
            current_user = account()
            current_user.deposit(username, user_deposit)
            clear()
            print(f"Your new balance is ${current_user.balance:.2f}")
            break
        else:
            print("Please give valid deposit amount!")

def withdraw(username):
    while True:
        user_widthdrawls = input("How much are you wanting to withdraw: $")
        if user_widthdrawls.isdigit():
            user_widthdrawls = float(user_widthdrawls)
            withdraw = 'Withdrawal'
            cur.execute('INSERT INTO info VALUES(?, ?, ?)', [username, withdraw, user_widthdrawls])
            current_user = account()
            current_user.withdraw(username, user_widthdrawls)
            clear()
            print(f"Your new balance is ${current_user.balance:.2f}")
            break
        else:
            print("Please give valid deposit amount!")   

def savings_account(username):
    while True:
        user_savings = input("How much are you wanting to put in your savings account?: $")
        if user_savings.isdigit():
            user_savings = float(user_savings)
            status = 'Moved to Savings'
            cur.execute('INSERT INTO info VALUES(?, ?, ?)', [username, status, user_savings])
            current_user = account()
            current_user.savings(username, user_savings)
            cur.execute('SELECT savings FROM users WHERE user_name = ?', [username])
            savings_balance = cur.fetchall()
            savings_balance = float(savings_balance[0][0])
            clear()
            print(f"Savings balance ${savings_balance:.2f}")
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
    

    

def transactions(username):
    cur.execute('SELECT status, transactions FROM info WHERE user_name = ?', [username])
    for info in cur.fetchall():
        print(f'{info[0]} - {info[1]}')

def change_password(username):
    clear()
    change = input("Would you like to change your password? [Y/N]: ").lower()
    if change == 'y':
        new_password = stdiomask.getpass(prompt = 'New Password: ')
        cur.execute('UPDATE users SET user_password = ? WHERE user_name = ?', [new_password, username])
        con.commit()
        print('Password Successfully Changed!')
    elif change == 'n':
        print('Returning to user options!')
    else:
        ('Please give valid input!')
