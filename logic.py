# vault
# api
# ai
# auth

from db import save_password, load_passwords, save_user, get_user
from utils import strength_generator, validate_username, validate_password, log_user, log_pass_saved
import hashlib
import requests

# login and sign up
class UserAuth:

    @staticmethod
    def hash_password(pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    def signup(self, username, password):
        if not validate_username(username):
            return False, 'Invalid username.'

        if not validate_password(password):
            return False, 'Your password may be too short.'

        hashed = self.hash_password(password)
        save_user(username, hashed)
        return True, 'User created.'

    def login(self, username, password):
        user = get_user(username)
        if not user:
            return False, 'User not found!'

        hashed = self.hash_password(password)
        if hashed != user[1]:
            return False, 'Wrong password!'
        
        log_user(username)
        return True, 'Login successful!'

# storing password
class PassVault:
    '''Basic password storage.'''

    def __init__(self, username):
        self.username = username

    def add_password(self, site, pwd):
        save_password(self.username, site, pwd)
        log_pass_saved(site, self.username)

    def get_all(self):
        rows = load_passwords(self.username)
        return sorted(rows, key=lambda x: x[0])
    
    def get_dict(self):
        rows = load_passwords(self.username)
        return {site: pwd for site, pwd in rows}

    def get_sites_set(self):
        rows = load_passwords(self.username)
        return {site for site, _ in rows}  

    def get_strength(self, pwd):
        return sum(strength_generator(pwd))

# api
def check_pwned(password):
    '''Returns number of times password appears in breaches.'''

    # 1. Hash password using SHA1
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    # 2. Query API with ONLY the prefix
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    if response.status_code != 200:
        return -1  # API unreachable

    hashes = response.text.splitlines()

    # 3. Look for the suffix in results
    for line in hashes:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return int(count)

    return 0  # Safe 

