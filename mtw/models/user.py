from mtw import mongo, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin


def add_user(email, password):
    password = generate_password_hash(
        password, method='pbkdf2:sha1', salt_length=8)
    mongo.db.users.insert_one({'email': email, 'password': password})


@login_manager.user_loader
def load_user(email):
    u = mongo.db.users.find_one({'email': email})
    if not u:
        return None
    return User(email)


class User(UserMixin):

    def __init__(self, email, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email

    def get_id(self):
        return self.email

    @classmethod
    def verify_password(self, password_hash, password):
        return check_password_hash(password_hash, password)

    @classmethod
    def get_user(cls, email):
        return mongo.db.users.find_one({'email': email})