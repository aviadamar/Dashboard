from http import HTTPStatus

import pytest

import db


class TestLogin:

    LOGIN_PAGE = '/login'
    POSSIBLE_WRONG_FIELDS = [
        ('', ''),
        ('boliisasnowman', 'lamili2020')
    ]

    @staticmethod
    def test_login_returns_ok(client):
        assert client.get(TestLogin.LOGIN_PAGE).status_code == HTTPStatus.OK

    @staticmethod
    @pytest.mark.parametrize("username,password", POSSIBLE_WRONG_FIELDS)
    def test_login_form_is_empty(username, password, client):
        data = {
            'username': username,
            'password': password
        }
        assert b'incorrect' in client.post(TestLogin.LOGIN_PAGE,
                                           data=data).data

    @staticmethod
    def test_login_successful(client, user, rowpassword):
        data = {
            'username': user.username,
            'password': rowpassword
        }

        page_data = client.post(TestLogin.LOGIN_PAGE, data=data)
        assert page_data.status_code == HTTPStatus.FOUND

    @staticmethod
    def test_login_not_successful(client):
        data = {
            'username': 'testadmin02',
            'password': 'testadmin2020',
        }

        page_data = client.post(TestLogin.LOGIN_PAGE, data=data)
        assert b'incorrect' in page_data.data
