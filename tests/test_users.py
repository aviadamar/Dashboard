
import db


class TestUsers:

    WRONG_USERNAME = "usernamethatnotexist"

    @staticmethod
    def test_delete_user(user):
        assert db.delete_user(user.username) == True

    @staticmethod
    def test_get_user(user):
        assert bool(db.get_user(user.username)) == True

    @staticmethod
    def test_not_get_user():
        assert db.get_user(TestUsers.WRONG_USERNAME) == False
