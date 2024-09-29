import requests
import allure

from config import BaseConfig as b
from data.data_orders import Orders as order
from order_generator import OrderGenerator as generator


class TestCreateOrder:

    @allure.title("Создаем заказ с токеном авторизации")
    def test_create_order_with_auth_token(self, get_jwt):
        jwt = get_jwt
        ingredients = {"ingredients": generator.build_burger()}
        response = requests.post(url=order.url, headers={"authorization": jwt}, data=ingredients)

        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.title("Создаем заказ без токена авторизации")
    def test_create_order_without_auth_token(self):
        ingredients = {"ingredients": generator.build_burger()}
        response = requests.post(url=order.url, data=ingredients)

        json = response.json()
        assert response.status_code == 200 and json["success"] is True

    @allure.title("Создаем заказ без ингридиентов")
    def test_create_order_without_ingredients(self):
        ingredients = {"ingredients": []}
        response = requests.post(url=order.url, data=ingredients)

        json = response.json()
        assert response.status_code == 400 and json["message"] == order.empty_ingredients_error

    @allure.title("Создаем заказ с несуществующим списком ингридиентов")
    def test_create_order_with_non_existing_ingredients(self):
        ingredients = {"ingredients": order.non_existing_ingredients}
        response = requests.post(url=order.url, data=ingredients)

        assert response.status_code == 500
