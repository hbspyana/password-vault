import sqlite3

DB_NAME = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            hashed TEXT
        )
    ''')

    c.execute('''
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
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES (?, ?)', (username, hashed))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    row = c.fetchone()
    conn.close()
    return row

def save_password(username, site, pwd):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO passwords (username, site, password) VALUES (?, ?, ?)',
              (username, site, pwd))
    conn.commit()
    conn.close()

def load_passwords(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT site, password FROM passwords WHERE username=?', (username,))
    rows = c.fetchall()
    conn.close()
    return rows
