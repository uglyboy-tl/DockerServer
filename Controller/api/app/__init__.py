# -*- coding:utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Test': 'My Uglyboy'}

api.add_resource(HelloWorld, '/api')
