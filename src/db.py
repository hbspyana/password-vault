import sqlite3

DB_NAME = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, hashed TEXT)') 
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords(       
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            site TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_user(username, hashed):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?)', (username, hashed))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,)) # * = get all columns
    user = cursor.fetchone()
    conn.close()
    return user

def save_password(username, site, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (username, site, password) VALUES (?, ?, ?)', (username, site, password))
    conn.commit()
    conn.close()

def load_passwords(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT site, password FROM passwords WHERE username=?', (username,))
    all_passwords = cursor.fetchall()
    conn.close()
    return all_passwords
