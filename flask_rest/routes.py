# routes.py
from flask_rest import app
from flask_restful import Resource, Api


api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
