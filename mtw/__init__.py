from flask import Flask
import flask.ext.mongoengine as mongoengine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {"DB": "localhost:27017"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = mongoengine.MongoEngine(app)


import mtw.views

if __name__ == '__main__':
    app.run()