from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

ns = api.namespace('hello', description='Hello operations')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """Fetch a hello world"""
        return {'hello': 'world!!!!!'}

if __name__ == '__main__':
    app.run(debug=True)
