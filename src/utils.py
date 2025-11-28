import logging
import re

logging.basicConfig(
    filename='logs.log',
    level='INFO', 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_pass_saved(site, user):
    logging.info(f'Password saved for "{site}" by {user}.')

def log_user(user):
    logging.info(f'{user} logged in.')

def validate_username(name):
    return bool(re.fullmatch(r'[A-Za-z0-9]{3,20}', name))

def validate_password(key):
    return bool(re.fullmatch(r'.{5,}', key))
