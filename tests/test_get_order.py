import pytest
import requests
import allure

from utils.endpoints import Urls
from utils.data import Ingredients, Responses

class TestGetOrder:
    @allure.title('Успешное получение заказов авторизованным пользователем')
    def test_get_order_auth_true(self,create_and_delete_user):
        make_order = requests.post(f'{Urls.URL}{Urls.MAKE_ORDER}', headers={'Authorization': create_and_delete_user[2]}, data=Ingredients.valid_ingredients)
        response = requests.get(f'{Urls.URL}{Urls.GET_ALL_ORDERS}', headers={'Authorization': create_and_delete_user[2]})
        assert response.status_code == 200 and 'true' in response.text

    @allure.title('Неуспешное получение заказов неавторизованным пользователем')
    def test_get_order_no_auth_fail(self):
        response = requests.get(f'{Urls.URL}{Urls.GET_ALL_ORDERS}')
        assert response.status_code == 401 and Responses.ERROR_GET_ORDER_NO_AUTH in response.text
