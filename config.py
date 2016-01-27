import os

class Config(object):

    SECRET_KEY = os.environ.get('FLASK_MTW_SECRET_KEY')
    MONGO_HOST = "ds035004.mongolab.com"
    MONGO_PORT = "35004"
    MONGO_DBNAME = "mtw"
    MONGO_USERNAME = "admin"
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class HerokuConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}