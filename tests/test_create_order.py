import pytest
import requests
from utils.endpoints import Urls
from utils.data import Responses, Ingredients
import allure

class TestCreateOrder:

    @allure.title('Успешное создание заказа авторизованным пользователем')
    def test_create_order_with_auth_true(self, create_and_delete_user):
        response = requests.post(f'{Urls.URL}{Urls.MAKE_ORDER}', headers={'Authorization': create_and_delete_user[2]}, data=Ingredients.valid_ingredients)
        assert response.status_code == 200 and 'true' in response.text

    @allure.title('Успешное создание заказа неавторизованным пользователем')
    def test_create_order_no_auth_true(self):
        response = requests.post(f'{Urls.URL}{Urls.MAKE_ORDER}', data=Ingredients.valid_ingredients)
        assert response.status_code == 200 and 'true' in response.text

    @allure.title('Неуспешное создание заказа без ингредиентов')
    def test_create_order_invalid_hash_fail(self):
        response = requests.post(f'{Urls.URL}{Urls.MAKE_ORDER}', data=Ingredients.invalid_ingredients)
        assert response.status_code == 500 and Responses.ERROR_WRONG_HASH in response.text

    @allure.title('Неуспешное создание заказа с невалидным хешем')
    def test_create_order_no_ingredients_fail(self):
        response = requests.post(f'{Urls.URL}{Urls.MAKE_ORDER}')
        assert response.status_code == 400 and Responses.ERROR_EMPTY_ORDER in response.text


