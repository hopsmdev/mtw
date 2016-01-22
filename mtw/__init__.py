import os
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager


app = Flask(__name__)

app.config["MONGO_HOST"] = "ds035004.mongolab.com"
app.config["MONGO_PORT"] = "35004"
app.config["MONGO_DBNAME"] = "mtw"
app.config["MONGO_USERNAME"] = "admin"
app.config["MONGO_PASSWORD"] = os.environ.get('MONGO_PASSWORD')

mongo = PyMongo(app, config_prefix="MONGO")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.view = 'login'


import mtw.views

if __name__ == '__main__':
    app.run()