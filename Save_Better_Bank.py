import sqlite3
import random
import stdiomask
from colorama import Fore, Back, Style
from os import system, name
from time import sleep
from Bank_Logic import cur, con, is_login_password_valid, deposits, withdraw, account, remove_account, clear, transactions, change_password
account = account()
def main_screen():
    while True:
        clear()
        print(Fore.CYAN + '''
        
      _____                   ____       _   _              ____              _    
     / ____|                 |  _ \     | | | |            |  _ \            | |   
    | (___   __ ___   _____  | |_) | ___| |_| |_ ___ _ __  | |_) | __ _ _ __ | | __
     \___ \ / _` \ \ / / _ \ |  _ < / _ \ __| __/ _ \ '__| |  _ < / _` | '_ \| |/ /
     ____) | (_| |\ V /  __/ | |_) |  __/ |_| ||  __/ |    | |_) | (_| | | | |   < 
    |_____/ \__,_| \_/ \___| |____/ \___|\__|\__\___|_|    |____/ \__,_|_| |_|_|\_\
                                                                                    
                                                                                    

        ''')
        main_menu = input("""What would you like to do?(Type Letter of what you want to do.)
        - a) Login
        - b) Create an account
        - c) Delete an existing account
        - d) Quit
        Type Here: """).lower()

        if main_menu == "a":
            clear()
            login()
            break
        elif main_menu == "b":
            clear()
            create_account()
        elif main_menu == "c":
            clear()
            remove_account()
        elif main_menu == "d":
            print("Goodbye!")
            quit()
        else:
            print("Please Try Again with a valid letter!")


class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def create_account():
    user_name = input(
        "Please provide a username you would like to use(Ex: ethan_bishop.20) - "
    )
    user_password = stdiomask.getpass(prompt = "Type a strong Password: ")
    completed_user = users(user_name, user_password)
    initial_balance = float(0)
    print(f"""
        Your User Name is {completed_user.name}, 
        Your password is {completed_user.password}, 
        """)
    cur.execute('INSERT INTO users VALUES(?, ?, ?)', (user_name, user_password, initial_balance))
    # cur.execute('INSERT INTO info VALUES(?)', (user_name))
    con.commit()
    print("Account Has Been Created!")
    clear()

def login():
    while True:
        user_login = input('UserName: ')
        user_password = stdiomask.getpass(prompt = 'Password: ')
        valid = is_login_password_valid(user_login, user_password)
        if valid == True:
            print('Successfully Logged in!')
            clear()
            while True:
                
                page = input("""Do you want to view balance, withdraw, deposit, or view transactions
        - a) View Balance
        - b) Deposit
        - c) Withdraw
        - d) View transactions
        - e) Change Password
        - f) Log out
        Type Here: """).lower()
                if page == "a":
                    clear()
                    account.view_balance(user_login)
                elif page == "b":
                    clear()
                    deposits(user_login)
                elif page == "c":
                    clear()
                    withdraw(user_login)
                elif page == "d":
                    clear()
                    transactions(user_login)
                elif page == "e":
                    clear()
                    change_password(user_login)
                    clear()
                elif page == "f":
                    clear()
                    print("Logged Out Successfully!")
                    main_screen()
                else:
                    print("Please Provide Valid Input!")
        else:
            option = input('Username or Password wrong! To TryAgain (T) or Exit with (E)\nInputHere: ').upper()
            if option == 'T':
                clear()
                login()
            elif option == 'E':
                clear()
                main_screen()
            else:
                ('Give valid input!')


main_screen()