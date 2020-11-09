import sqlite3
import Bank_Logic
print("Welcome to SaveBetterBank(SBB)")
main_menu = input("""What would you like to do?
    - Login
    - Create an account
    - Delete an existing account
    Type Here: """
)

class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password



