import sqlite3

con = sqlite3.connect('Save_Better_Bank.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users(user_name TEXT, user_password TEXT)')
con.commit()
