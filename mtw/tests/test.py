import unittest
import flask
from flask.ext.pymongo import PyMongo


def set_default_db(app):
    app.config["MONGO_HOST"] = "ds035004.mongolab.com"
    app.config["MONGO_PORT"] = "35004"
    app.config["MONGO_DBNAME"] = "mtw"
    app.config["MONGO_USERNAME"] = "admin"
    app.config["MONGO_PASSWORD"] = "admin"


class MongoDbTest(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask('test')
        self.context = self.app.test_request_context('/')
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_default_config_prefix(self):
        set_default_db(self.app)

        mongo = PyMongo(self.app)
        self.assertEqual(mongo.db.name, 'mtw')

    def test_get_one_user(self):
        set_default_db(self.app)
        mongo = PyMongo(self.app)
        user = mongo.db.users.find_one({"email": "test@test.com"})
        print(user['email'])
        print(user['password'])


if __name__ == "__main__":
    unittest.main()