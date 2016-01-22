from werkzeug.security import check_password_hash


class UserLogin(object):

    def __init__(self, email):
        self.email = email

    @classmethod
    def is_authenticated(self):
        return True

    @classmethod
    def is_active(self):
        return True

    @classmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)