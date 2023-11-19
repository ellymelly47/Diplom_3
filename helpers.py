import requests
import random
import string


def generate_login():
    number = random.randint(1000, 9999)
    email = f'test_testoviy_{number}@ya.ru'
    return email


def generate_password(length=6):
    alphabet = string.ascii_letters + string.digits
    password = ''
    for _ in range(length):
        password += random.choice(alphabet)
    return password


def generate_username(length=5):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name


def user():
    payload = {
        'email': generate_login(),
        'password': generate_password(length=6),
        'name': generate_username(length=5)
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    assert response.status_code == 200
    return payload
