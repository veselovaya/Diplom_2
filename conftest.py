import pytest
import requests

from utils.endpoints import Urls
from utils.data import UserData


@pytest.fixture(scope="function")
def create_and_delete_user():
    payload = UserData.create_user_data()
    response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
    token = response.json()["accessToken"]
    yield response, payload, token
    requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': f'{token}'})



