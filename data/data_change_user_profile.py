from config import BaseConfig as b


class ChangeUserProfile:
    method = "/api/auth/user"
    url = b.base_url + method

    not_authorize_user_error = "You should be authorised"
