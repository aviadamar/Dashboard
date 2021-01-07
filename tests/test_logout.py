from http import HTTPStatus


class TestLogout:

    LOGIN_PAGE = '/login'
    LOGOUT_PAGE = '/logout'

    @staticmethod
    def test_logout_successful(client, user, rowpassword):
        data = {
            'username': user.username,
            'password': rowpassword
        }

        client.post(TestLogout.LOGIN_PAGE, data=data)
        assert client.get(
            TestLogout.LOGOUT_PAGE).status_code == HTTPStatus.FOUND
