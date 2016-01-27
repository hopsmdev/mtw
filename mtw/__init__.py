import os
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
from config import config


mongo = PyMongo()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mongo.init_app(app)
    login_manager.init_app(app)

    return app