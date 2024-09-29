from config import BaseConfig as b


class Login:
    method = "/api/auth/login"
    url = b.base_url + method

    existing_user = {
        'email': 'gubanov12qa@yandex.ru',
        'password': 'fRodoAndBilbo'
    }

    not_existing_user = {
        'email': 'farfarelle@example.net',
        'password': '00000012'
    }

    error_not_existing_user = "email or password are incorrect"
