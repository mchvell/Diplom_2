import allure

from faker import Faker


class UserData:
    @staticmethod
    def generate_name():
        faker = Faker('ru_RU')
        return faker.name()

    @staticmethod
    def generate_email():
        faker = Faker('ru_RU')
        return faker.email()

    @staticmethod
    def generate_password():
        faker = Faker('ru_RU')
        return str(faker.password())

    @staticmethod
    @allure.step("Генерируем пользовательские данные и собираем в словарь")
    def generate_user_credentials():
        name = UserData.generate_name()
        email = UserData.generate_email()
        password = UserData.generate_password()
        return {
            "name": name,
            "email": email,
            "password": password
        }
