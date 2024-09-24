from config import BaseConfig as b


class ChangeUserProfile:
    method = "/api/auth/user"
    url = b.base_url + method

    existing_user = {
        'email': 'gubanov12qa@yandex.ru',
        'name': 'Миша'
    }

    not_authorize_user_error = "You should be authorised"
