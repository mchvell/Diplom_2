import allure
import requests

from config import BaseConfig as b
from user_generator import UserData as generator
from data.data_change_user_profile import ChangeUserProfile as change


class TestChangeUserProfile:

    @allure.description("Изменяем имя для существующего юзера с токеном авторизации")
    def test_change_name_for_existing_user_with_auth_token(self):
        user_data = change.existing_user
        user_data["name"] = generator.generate_name()
        response = requests.patch(url=change.url, headers={"authorization": b.authorization}, data=user_data)

        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.description("Изменяем имя для существующего юзера без токена авторизации")
    def test_change_name_for_existing_user_without_auth_token(self):
        user_data = change.existing_user
        user_data["name"] = generator.generate_name()
        response = requests.patch(url=change.url, data=user_data)

        json = response.json()
        assert response.status_code == 401 and json["message"] == change.not_authorize_user_error


