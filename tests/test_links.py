
import db


class TestLinks:

    URL_NAME = 'test02'
    URL_CHECK = 'https://www.test02.com'

    @staticmethod
    def test_get_link(link):
        assert bool(db.get_link(link.url)) == True

    @staticmethod
    def test_create_link(user):
        link = db.get_link(TestLinks.URL_CHECK)
        if link:
            db.delete_link(link.id)

        name = TestLinks.URL_NAME
        url = TestLinks.URL_CHECK
        description = 'test'
        username = user.username

        assert bool(db.create_link(name, url, description, username)) == True

    @staticmethod
    def test_delete_link(link):
        assert db.delete_link(link.id) == True

    @staticmethod
    def test_not_get_link():
        url = "www.notaurl.com"
        assert db.get_link(url) == False

    @staticmethod
    def test_add_to_board(link, user):
        assert db.add_to_board(link, user.username) == True
