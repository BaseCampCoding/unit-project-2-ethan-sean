import sqlite3
import random
from Bank_Logic import cur, con, is_login_password_valid
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
            self.balance -= withdraw

    def total_balance(self):
        return self.balance

def create_account():
    user_name = input(
        "Please provide a username you would like to use(Ex: ethan_bishop.20) - "
    )
    user_password = input("Type a strong Password: ")
    completed_user = users(user_name, user_password)
    user_id = random.randint(100000, 999999)
    print(f"""
        Your User Name is {completed_user.name}, 
        Your password is {completed_user.password}, 
        Your account number is {user_id}
        """)
    cur.execute('INSERT INTO users VALUES(?, ?, ?)', (user_name, user_password, user_id))
    cur.execute('INSERT INTO account VALUES(?)', (user_id))
    con.commit()
    print("Account Has Been Created!")

def login_page():
    while True:
        page = input("""Do you want to view balance, withdraw, deposit, or view transactions
        - a) View Balance
        - b) Deposit
        - c) Withdraw
        - d) View transactions
        - e) Log Out
        Type Here: """).lower()
        if page == "a":
            view_balance()
        elif page == "b":
            deposits()
        elif page == "b":
            widthdrawls()
        elif page == "d":
            transactions()
        elif page == "e":
            print("Logged Out Successfully!")
            quit()
        else:
            print("Please Provide Valid Input!")
    


print("Welcome to SaveBetterBank(SBB)")

def login():
    while True:
        user_login = input('UserName: ')
        user_password = input('Password: ')
        valid = is_login_password_valid(user_login, user_password)
        if valid == True:
            print('Successfully Logged in!')
            login_page()
            break
        else:
            print('Username or password wrong. Try Again!')

def valid_number(num):
    while True:
        response = input(num)
        if response.isdigit():
            response = int(num)
            if response >= 0:
                return response
        print("Please provide a valid number")

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