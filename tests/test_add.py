from http import HTTPStatus

import db


class TestAdd:

    ADD_PAGE = '/add'
    INDEX = '/'

    @staticmethod
    def test_add_get(client):
        assert client.get(
            TestAdd.ADD_PAGE).status_code == HTTPStatus.FOUND

    @staticmethod
    def test_add_post(client, user, link):
        with client.session_transaction() as sess:
            sess['username'] = user.username

        data = {
            'name': link.name,
            'url': link.url,
            'description': link.description,
        }
        db.delete_link(link.id)

        client.post(TestAdd.ADD_PAGE, data=data).data
        assert data['name'].encode('utf-8') in client.get(TestAdd.INDEX).data
