from faker import Faker


class UserData:
    @staticmethod
    def create_user_data():
        fake = Faker()
        user_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return user_data

    @staticmethod
    def generate_name():
        fake = Faker()
        name = fake.name()
        return name

    @staticmethod
    def generate_email():
        fake = Faker()
        email = fake.email()
        return email

    @staticmethod
    def generate_password():
        fake = Faker()
        password = fake.password()
        return password


class InvalidData:
    dublicate_data = {
        "email": "test6135@ya.ru",
        "password": "test123",
        "name": "TestUser"
    }

    data_no_name = {
        "email": "test6135@ya.ru",
        "password": "test123",
        "name": ""
    }

    data_no_email = {
        "email": "",
        "password": "test123",
        "name": "TestUser"
    }

    data_no_password = {
        "email": "test6135@ya.ru",
        "password": "",
        "name": "TestUser"
    }

    data_with_mistake_email = {
        "email": "testt6135@ya.ru",
        "password": "test123"
    }

    data_with_mistake_pass = {
        "email": "test6135@ya.ru",
        "password": "testt123"
    }

class Responses:
    ERROR_USER_EXISTS = "User already exists"
    ERROR_CREATE_USER_NO_PARAM = "Email, password and name are required fields"
    ERROR_UPDATE_NO_AUTH = "You should be authorised"
    ERROR_LOGIN_INVALID_DATA =  "email or password are incorrect"
    ERROR_EMPTY_ORDER = "Ingredient ids must be provided"
    ERROR_WRONG_HASH = "Internal Server Error"


class Ingredients:
    valid_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    invalid_ingredients = {
        "ingredients": ["61c0c5a71d1", "61c0c5a71d1f"]
    }
