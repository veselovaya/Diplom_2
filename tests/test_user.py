import pytest
import requests
from utils.endpoints import Urls
from utils.data import UserData, InvalidData, Responses



class TestCreateUser:

    def test_user_register_true(self):
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=UserData.create_user_data())
        assert response.status_code == 200 and 'true' in response.text

    def test_double_user_register_fail(self):
        exist_user_data = InvalidData.dublicate_data
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=exist_user_data)
        assert response.status_code == 403 and Responses.ERROR_USER_EXISTS in response.text

    @pytest.mark.parametrize(
        'invalid_data',
        [InvalidData.data_no_name, InvalidData.data_no_email, InvalidData.data_no_password]
    )
    def test_user_register_invalid_data_fail(self, invalid_data):
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=invalid_data)
        assert response.status_code == 403 and Responses.ERROR_CREATE_USER_NO_PARAM in response.text


class TestLoginUser:

    def test_exist_user_login_true(self, create_and_delete_user):
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_USER}', data=create_and_delete_user[1])
        assert response.status_code == 200 and 'true' in response.text

    @pytest.mark.parametrize(
        'mistake_data',
        [InvalidData.data_with_mistake_email, InvalidData.data_with_mistake_pass]
    )
    def test_invalid_data_login_fail(self, mistake_data):
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_USER}', data=mistake_data)
        assert response.status_code == 401 and Responses.ERROR_LOGIN_INVALID_DATA in response.text


class TestUpdateUser:

    def test_update_name_with_auth_true(self,create_and_delete_user):
        new_name = {"name": UserData.generate_name()}
        response = requests.patch(f'{Urls.URL}{Urls.EDIT_USER_DATA}', headers={'Authorization':create_and_delete_user[2]}, data=new_name)
        assert response.status_code == 200 and 'true' in response.text

    def test_update_email_with_auth_true(self,create_and_delete_user):
        new_email = {"email": UserData.generate_email()}
        response = requests.patch(f'{Urls.URL}{Urls.EDIT_USER_DATA}', headers={'Authorization':create_and_delete_user[2]}, data=new_email)
        assert response.status_code == 200 and 'true' in response.text

    def test_update_pass_with_auth_true(self,create_and_delete_user):
        new_pass = {"password": UserData.generate_password()}
        response = requests.patch(f'{Urls.URL}{Urls.EDIT_USER_DATA}', headers={'Authorization':create_and_delete_user[2]}, data=new_pass)
        assert response.status_code == 200 and 'true' in response.text

    @pytest.mark.parametrize(
        'update_data',
        [
            {"email": UserData.generate_email()},
            {"password": UserData.generate_password()},
            {"name": UserData.generate_name()}
        ]
    )
    def test_update_data_no_auth_fail(self,update_data):
        response = requests.patch(f'{Urls.URL}{Urls.EDIT_USER_DATA}', data=update_data)
        assert response.status_code == 401 and Responses.ERROR_UPDATE_NO_AUTH in response.text