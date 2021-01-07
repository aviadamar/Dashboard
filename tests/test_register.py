from http import HTTPStatus

import pytest

import db

CHECK_USER = ('testadmin', 'testadmin2020')


def delete_check_user(CHECK_USER):
    username = CHECK_USER[0]
    if db.get_user(username):
        db.delete_user(username)


class TestRegister:

    SUCCESS_MASSAGE = b'Successful'
    REGISTER_PAGE = '/register'

    @staticmethod
    def test_create_user_success(client):
        delete_check_user(CHECK_USER)
        data = {
            'username': 'testadmin',
            'email': 'testadmin@gmail.com',
            'password': 'testadmin2020',
            'password_validation': 'testadmin2020'
        }

        assert TestRegister.SUCCESS_MASSAGE in client.post(
            TestRegister.REGISTER_PAGE, data=data).data

    @staticmethod
    def test_create_user_not_success(client):
        data = {
            'username': 'aviad$$2020',
            'email': 'aviad@gmail.com',
            'password': 'aviad2020',
            'password_validation': 'aviad2020'
        }

        assert TestRegister.SUCCESS_MASSAGE not in client.post(
            TestRegister.REGISTER_PAGE, data=data).data

    @staticmethod
    def test_is_valid_password(passwords):
        for password in passwords['valid']:
            assert bool(db.is_valid_password(password)) == True

        for password in passwords['invalid']:
            assert bool(db.is_valid_password(password)) == False

    @staticmethod
    def test_is_valid_email(emails):
        for email in emails['valid']:
            assert bool(db.is_valid_email(email)) == True

        for email in emails['invalid']:
            assert bool(db.is_valid_email(email)) == False

    @staticmethod
    def test_is_valid_username(usernames):
        for user in usernames['valid']:
            assert bool(db.is_valid_username(user)) == True

        for user in usernames['invalid']:
            assert bool(db.is_valid_username(user)) == False
