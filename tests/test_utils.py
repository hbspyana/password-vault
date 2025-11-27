from utils import validate_username, validate_password, list, strength_generator

def test_validate_username():
    assert validate_username("abc123")
    assert not validate_username("!@#$%")
    assert not validate_username("hi")
    assert validate_username("UserName20")

def test_validate_password():
    assert validate_password("12345")
    assert not validate_password("1234")
    assert validate_password("abcdefghijklmnop12345")

def test_strength_generator():
    pwd = "Hi1"
    gen = strength_generator(pwd)
    results = list(gen)
    assert sum(results) > 0
    assert len(results) == len(pwd)
