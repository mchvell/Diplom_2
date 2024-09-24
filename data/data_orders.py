import random


from config import BaseConfig as b


class Orders:
    method = "/api/orders"
    url = b.base_url + method

    non_existing_ingredients = ["пюрешка", "котлетки", "лучок"]

    empty_ingredients_error = "Ingredient ids must be provided"

    non_auth_user_error = "You should be authorised"
