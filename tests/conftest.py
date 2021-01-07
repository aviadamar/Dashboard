
import os
import tempfile
from datetime import date
import pytest

from app import app
import db


URL_NAME = 'test02'
URL_CHECK = 'https://www.test02.com'


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    # app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def user():
    if db.get_user('testadmin'):
        db.delete_user('testadmin')
    user = db.create_user(
        'testadmin',
        'testadmin@gmail.com',
        'testadmin2020'
    )
    yield user


@pytest.fixture
def link(user):
    is_link = db.get_link(URL_CHECK)
    if is_link:
        db.delete_link(is_link.id)

    name = URL_NAME
    url = URL_CHECK
    description = 'test'
    username = user.username
    yield db.create_link(name, url, description, username)


@pytest.fixture
def rowpassword():
    return 'testadmin2020'


@pytest.fixture
def passwords():
    valid = ('loli2020', 'lama-ani1988')
    invalid = ('1988', 'lover3')
    return {'valid': valid,  'invalid': invalid}


@pytest.fixture
def emails():
    valid = ('avilama@walla.com', 'shani_lamar@gmail.com')
    invalid = ('aviad@gmail@com', '$hello@gmail.com')
    return {'valid': valid,  'invalid': invalid}


@pytest.fixture
def usernames():
    valid = ('yammesika', '2020loliamar')
    invalid = ('Shlomi@amar', 'a' * 21)
    return {'valid': valid,  'invalid': invalid}
