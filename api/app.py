import os
from flask import Flask
from redis import Redis
from flask_restful import Api

from . import db
from .resources import HelloResource

def create_app(test_config=None):
    app = Flask(__name__)
    api = Api(app)

    with app.app_context():
        db.init_app(app)
        api.add_resource(HelloResource, '/')

    return app
