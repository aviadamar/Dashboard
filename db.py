import dconfig
from datetime import date
import hashlib
import os
from peewee import *


database = PostgresqlDatabase(dconfig.DATABASE_URL)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(unique=True)
    salt = BlobField()
    password = BlobField()
    email = CharField(unique=True)
    added_date = DateTimeField()
    theme = IntegerField()
    followers = IntegerField()
    level = IntegerField()


class Link(BaseModel):
    name = CharField(unique=True)
    url = CharField(unique=True)
    logo_url = CharField(null=True)
    description = CharField(null=True)
    added_date = DateTimeField()
    followers = IntegerField()


class UserLink(BaseModel):
    user_id = ForeignKeyField(User)
    link_id = ForeignKeyField(Link)


def create_tables():
    database.create_tables([User, Link, UserLink])


def create_user(username, email, password):
    hash_pass = hash_password(password)
    user = User.create(
        username=username,
        salt=hash_pass[0],
        password=hash_pass[1],
        email=email,
        added_date=date.today(),
        theme=0,
        followers=0,
        level=1
    )
    user.save()


def create_link(name, url, description, username):
    if name is None or len(name) > 20 or url is None:
        return False
    if not "https://" in url:
        url = "https://" + url

    link = get_link(url)
    if not link:
        link = Link.create(
            name=name.lower(),
            url=url,
            logo_url=None,
            description=description.lower(),
            added_date=date.today(),
            followers=0
        )
        link.save()

    if not get_user(username).level == 100:
        return add_to_board(link, username)


def get_user(username):
    try:
        user = User.select().where(User.username == username).get()
    except (DoesNotExist, NameError):
        return False
    return user


def get_link(url):
    try:
        link = Link.select().where(Link.url == url).get()
    except (DoesNotExist, NameError):
        return False
    return link


def get_user_links(username):
    user = get_user(username)
    if user.level == 100:
        all_links = Link.select()
    else:
        all_links = [
            Link.select().where(Link.id == link.link_id).get()
            for link in UserLink.select().where(UserLink.user_id == user.id)
        ]
    return all_links


def update_followers(link_id, remove=False):
    link = Link.select().where(Link.id == link_id).get()
    if remove and link.followers > 0:
        link.followers -= 1
    else:
        link.followers += 1
    link.save()


def add_to_board(new_link, username):
    user = get_user(username)
    try:
        link = UserLink.select().where(
            UserLink.user_id == user.id, UserLink.link_id == new_link.id).get()
    except DoesNotExist:
        new_row = UserLink(
            user_id=user.id,
            link_id=new_link.id
        )
        new_row.save()
        update_followers(new_link.id, remove=False)
        return True
    return False


def remove_from_board(link_id, username):
    user = get_user(username)
    if not user.level == 100:
        link = UserLink.select().where(
            UserLink.user_id == user.id, UserLink.link_id == link_id).get()
        link.delete_instance()
        update_followers(link_id, remove=True)
    else:
        link = Link.select().where(Link.id == link_id).get()
        link.delete_instance()


def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(
        'utf-8'), salt, 100000, dklen=128)
    return salt, key


def verify_password(user, user_input):
    salt = user.salt.tobytes()
    key = user.password.tobytes()
    reversed_key = hashlib.pbkdf2_hmac(
        'sha256', user_input.encode('utf-8'), salt, 100000, dklen=128)
    return reversed_key == key


def is_password_currect(password):
    for char in password:
        if not (char.isalpha() or char.isdigit()):
            return False
    return True


def is_valid_email(email):
    return True


def registration_validation(status,  username, email,
                            password, password_validation):
    if get_user(username):
        status['available_username'] = False

    if not (8 < len(username) < 20):
        status['valid_username'] = False

    if not is_valid_email(email):
        status['valid_email'] = False

    if not is_password_currect(password):
        status['valid_password'] = False
    elif not password == password_validation:
        status['password_validation'] = False

    return status
