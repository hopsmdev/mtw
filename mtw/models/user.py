from mtw import mongo, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin, AnonymousUserMixin


def get_user(email):
    return mongo.db.users.find_one({'email': email})


def add_user(email, password):
    password = generate_password_hash(
        password, method='pbkdf2:sha1', salt_length=8)
    mongo.db.users.insert_one({'email': email, 'password': password})


@login_manager.user_loader
def load_user(user_id):
    return mongo.db.users.find_one({'_id': user_id})


class UserLogin(UserMixin):

    def __init__(self, email):
        self.email = email

    def get_id(self):
        return self.email

    @classmethod
    def validate_login(cls, password_hash, password):
        return check_password_hash(password_hash, password)