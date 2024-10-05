import allure
import requests

from user_generator import UserData as generator
from data.data_change_user_profile import ChangeUserProfile as change
from data.data_login import Login as login


class TestChangeUserProfile:

    @allure.title("Изменяем для юзера, которого создаем")
    def test_change_name_for_existing_user_with_auth_token(self, create_unique_user):
        jwt = create_unique_user
        user_data = {
            "name": generator.generate_name(),
            "email": generator.generate_email()
        }
        response = requests.patch(url=change.url, headers={"authorization": jwt}, data=user_data)

        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.title("Изменяем имя для существующего юзера без токена авторизации")
    def test_change_name_for_existing_user_without_auth_token(self):
        user_data = login.existing_user
        user_data["name"] = generator.generate_name()
        response = requests.patch(url=change.url, data=user_data)

        json = response.json()
        assert response.status_code == 401 and json["message"] == change.not_authorize_user_error


