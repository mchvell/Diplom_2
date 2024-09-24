import requests

from config import BaseConfig as b
from data.data_orders import Orders as order


class TestGetOrder:
    def test_get_user_orders_with_auth(self):
        response = requests.get(url=order.url, headers={"authorization": b.authorization})

        json = response.json()
        assert response.status_code == 200 and len(json["orders"]) > 1

    def test_get_user_orders_without_auth(self):
        response = requests.get(url=order.url)

        json = response.json()
        assert response.status_code == 401 and json["message"] == order.non_auth_user_error

