import allure
import requests

from data.data_orders import Orders as order


class TestGetOrder:
    @allure.title("Получаем заказы авторизованного пользователя")
    def test_get_user_orders_with_auth(self, get_jwt):
        jwt = get_jwt
        response = requests.get(url=order.url, headers={"authorization": jwt})

        json = response.json()
        assert response.status_code == 200 and len(json["orders"]) > 0

    @allure.title("Пробуем получить заказы без авторизации")
    def test_get_user_orders_without_auth(self):
        response = requests.get(url=order.url)

        json = response.json()
        assert response.status_code == 401 and json["message"] == order.non_auth_user_error

