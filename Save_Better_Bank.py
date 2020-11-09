import sqlite3
import Bank_Logic

class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login_info(self):
        return self.name, self.password
    

def create_account():
    user_name = input("Please provide a username you would like to use(Ex: ethan_bishop.20) - ")
    user_password = input("Type a strong Password: ")
    completed_user = users(user_name, user_password)
    print(f"Your User Name is [{completed_user.name}], Your password is [{completed_user.password}]")
    print("Account Has Been Created!")


print("Welcome to SaveBetterBank(SBB)")
main_menu = input("""What would you like to do?(Type Letter of what you want to do.)
    - a) Login
    - b) Create an account
    - c) Delete an existing account
    Type Here: """
)

while True:
    if main_menu == "a":
        login()
        break
    elif main_menu == "b":
        create_account()
        break
    elif main_menu == "c":
        remove_account()
        break
    else:
        


balance = 0
class account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, deposit):
        self.deposit = self.deposit + balance
    
    def withdraw(self, withdraw):
        if self.balance >= amount:
            self.withdraw - balance
