import sqlite3
import random
from Bank_Logic import cur, con, is_login_password_valid, deposits, view_balance, widthdrawls
class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def create_account():
    user_name = input(
        "Please provide a username you would like to use(Ex: ethan_bishop.20) - "
    )
    user_password = input("Type a strong Password: ")
    completed_user = users(user_name, user_password)
    initial_balance = float(0)
    print(f"""
        Your User Name is {completed_user.name}, 
        Your password is {completed_user.password}, 
        """)
    cur.execute('INSERT INTO users VALUES(?, ?, ?)', (user_name, user_password, initial_balance))
    con.commit()
    print("Account Has Been Created!")

# def login_page():
#     while True:
#         page = input("""Do you want to view balance, withdraw, deposit, or view transactions
#         - a) View Balance
#         - b) Deposit
#         - c) Withdraw
#         - d) View transactions
#         - e) Log Out
#         Type Here: """).lower()
#         if page == "a":
#             view_balance()
#         elif page == "b":
#             deposits()
#         elif page == "b":
#             widthdrawls()
#         elif page == "d":
#             transactions()
#         elif page == "e":
#             print("Logged Out Successfully!")
#             quit()
#         else:
#             print("Please Provide Valid Input!")
    
# print("Welcome to SaveBetterBank(SBB)")

def login():
    while True:
        user_login = input('UserName: ')
        user_password = input('Password: ')
        valid = is_login_password_valid(user_login, user_password)
        if valid == True:
            print('Successfully Logged in!')
            while True:
                page = input("""Do you want to view balance, withdraw, deposit, or view transactions
                - a) View Balance
                - b) Deposit
                - c) Withdraw
                - d) View transactions
                - e) Log Out
                Type Here: """).lower()
                if page == "a":
                    view_balance(user_login)
                elif page == "b":
                    deposits(user_login)
                elif page == "b":
                    widthdrawls(user_login)
                elif page == "d":
                    transactions()
                elif page == "e":
                    print("Logged Out Successfully!")
                    quit()
                else:
                    print("Please Provide Valid Input!")
        else:
            print('Username or password wrong. Try Again!')


while True:
    main_menu = input("""What would you like to do?(Type Letter of what you want to do.)
    - a) Login
    - b) Create an account
    - c) Delete an existing account
    Type Here: """).lower()

    if main_menu == "a":
        login()
        break
    elif main_menu == "b":
        create_account()
    elif main_menu == "c":
        remove_account()
        break
    else:
        print("Please Try Again with a valid letter!")

# user = account()
# user1 = user.deposit(50)
# user1 = user.withdraw(20)

# user2 = account()
# user = user2.deposit(100)
# user = user2.withdraw(10)
# # print(user2)
# print(f"Your balance is ${user.balance:.2f}")
# print(f"Your balance is ${user2.balance:.2f}")