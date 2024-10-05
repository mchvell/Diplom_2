import allure
import pytest
import requests
from data.data_login import Login as log
from user_generator import UserData as user
from data.data_create_user import CreateUser as reg


@allure.step("Получить токен авторизации для существвуюшего юзера")
@pytest.fixture(scope="function")
def get_jwt():
    response = requests.post(url=log.url, data=log.existing_user)
    json = response.json()
    return json["accessToken"]


@allure.step("Создать нового пользователя и получить его токен авторизации")
@pytest.fixture(scope="function")
def create_unique_user():
    user_credentials = user.generate_user_credentials()
    response = requests.post(url=reg.url, data=user_credentials)
    json = response.json()
    return json["accessToken"]

