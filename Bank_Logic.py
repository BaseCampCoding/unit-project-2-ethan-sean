import sqlite3

con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT, user_id INT)')

cur.execute('CREATE TABLE IF NOT EXISTS accounts(user_id INT, balance REAL, transactions TEXT)')
con.commit()

def is_login_password_valid(username: str, password: str) -> bool:
    cur.execute('SELECT * FROM users WHERE user_name = ? AND user_password = ?', [username, password])
    if cur.fetchall():
        return True
    else:
        return False