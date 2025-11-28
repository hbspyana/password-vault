# vault
# api
# ai
# auth

from db import save_password, load_passwords, save_user, get_user
from utils import validate_username, validate_password, log_user, log_pass_saved
import hashlib
import requests

# login and sign up
class UserAuth:
    
    @staticmethod
    def hash_password(key):
        return hashlib.sha256(key.encode()).hexdigest()

    def signup(self, username, password):
        if not validate_username(username):
            return False, 'Invalid username.'

        if not validate_password(password):
            return False, 'Your password is too short.'

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
    def __init__(self, username):
        self.username = username

    def add_password(self, site, key):
        save_password(self.username, site, key)
        log_pass_saved(site, self.username)

    def get_all(self):
        rows = load_passwords(self.username)
        return sorted(rows, key=lambda x: x[0])

    def get_strength(self, key):
        return sum(strength_generator(key))

# check leaks (api)
def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    if response.status_code != 200:
        return False

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return int(count)

    return True

