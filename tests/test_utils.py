from utils import validate_username, validate_password

def test_validate_username():
    assert validate_username("abc123")
    assert not validate_username("!@#$%")
    assert not validate_username("hi")
    assert validate_username("Username123")

def test_validate_password():
    assert validate_password("12345")
    assert not validate_password("1234")
    assert validate_password("abcdefghijklmnop12345")
