import random
import allure


class OrderGenerator:
    breads = {
        "flouriscrent_bread": "61c0c5a71d1f82001bdaaa6d",
        "krator_bread": "61c0c5a71d1f82001bdaaa6c"
    }

    sauces = {
        "spicy_x": "61c0c5a71d1f82001bdaaa72",
        "space": "61c0c5a71d1f82001bdaaa73",
        "traditional": "61c0c5a71d1f82001bdaaa74",
        "thorns": "61c0c5a71d1f82001bdaaa75"
    }

    fillings = {
        "moluskus_patty": "61c0c5a71d1f82001bdaaa6f",
        "beef_patty": "61c0c5a71d1f82001bdaaa70",
        "magnolia_patty": "61c0c5a71d1f82001bdaaa71",
        "tetradoform_patty": "61c0c5a71d1f82001bdaaa6e",
        "mineral_rings": "61c0c5a71d1f82001bdaaa76",
        "fellenial_tree_goods": "61c0c5a71d1f82001bdaaa77",
        "marsian_alpha_sugar": "61c0c5a71d1f82001bdaaa78",
        "salad": "61c0c5a71d1f82001bdaaa79",
        "asteroid_cheese": "61c0c5a71d1f82001bdaaa7a"
    }

    @classmethod
    @allure.step("Создание бургера со случайным набором ингридиентов")
    def build_burger(cls):
        bread = random.choice(list(cls.breads.values()))

        sauces = random.sample(list(cls.sauces.values()), random.randint(0, len(cls.sauces)))

        fillings = random.sample(list(cls.fillings.values()), random.randint(0, len(cls.fillings)))

        burger = [bread] + sauces + fillings

        return burger
