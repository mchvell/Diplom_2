from config import BaseConfig as b


class CreateUser:
    method = "/api/auth/register"
    url = b.base_url + method

    existing_user = {
        'email': 'anzhela51@example.net',
        'name': 'Зосима Еремеевич Устинов',
        'password': '&1mQaWEa&6'
    }

    error_user_already_exist = "User already exists"

    error_lost_credentials_field = "Email, password and name are required fields"
