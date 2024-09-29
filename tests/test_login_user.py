import requests
import allure

from data.data_login import Login as log


class TestCreateUser:

    @allure.title("Авторизация юзера с валидными креденшиалс")
    def test_login_with_existing_user(self):
        response = requests.post(url=log.url, data=log.existing_user)
        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.title("Авторизация не существующего юзера")
    def test_login_with_not_existing_user(self):
        response = requests.post(url=log.url, data=log.not_existing_user)
        json = response.json()
        assert response.status_code == 401 and json["message"] == log.error_not_existing_user

