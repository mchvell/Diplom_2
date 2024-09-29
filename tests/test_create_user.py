import requests
import allure

from data.data_create_user import CreateUser as reg
from user_generator import UserData as user


class TestCreateUser:

    @allure.title("Создаем нового юзера со случайными данными")
    def test_create_unique_user(self):
        user_credentials = user.generate_user_credentials()
        response = requests.post(url=reg.url, data=user_credentials)
        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.title("Создаем нового юзера с существующими данными")
    def test_create_user_with_existing_credentials(self):
        user_credentials = reg.existing_user
        response = requests.post(url=reg.url, data=user_credentials)
        json = response.json()
        assert response.status_code == 403 and json["message"] == reg.error_user_already_exist

    @allure.title("Создаем нового юзера с пустой строкой имя")
    def test_create_user_with_one_empty_field(self):
        user_credentials = user.generate_user_credentials()
        user_credentials["name"] = ""
        response = requests.post(url=reg.url, data=user_credentials)
        json = response.json()
        assert response.status_code == 403 and json["message"] == reg.error_lost_credentials_field

