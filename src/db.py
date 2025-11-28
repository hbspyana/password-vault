import sqlite3

DB_NAME = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, hashed TEXT)') 
    # creates a table. columns: username, hashed. "primary key" means no duplicates. stores hashed password as text.
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords(       
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            site TEXT,
            password TEXT
        )
    ''') # creates a table. columns: id, username, site, password(unhashed). id is an integer(not text) primary key and autoincremented(1,2,3...).

    conn.commit()
    conn.close()

def save_user(username, hashed):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?)', (username, hashed)) # add a new row with username and hashed pass. (?, ?) prevents hacking
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,)) # get all columns (*) equal to given user. check if user exists
    user = cursor.fetchone()
    conn.close()
    return user

def save_password(username, site, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (username, site, password) VALUES (?, ?, ?)', (username, site, password)) # inserts data into 3 columns
    conn.commit()
    conn.close()

def load_passwords(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT site, password FROM passwords WHERE username=?', (username,)) # gets all site, password columns that belong to specified user
    all_passwords = cursor.fetchall()
    conn.close()
    return all_passwords
