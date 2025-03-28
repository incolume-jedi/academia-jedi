"""Module."""

import os

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    """HelloWord class."""

    def get(self):
        """Get it."""
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=os.environ['AJEDII_DEBUG_MODE'])

# para testar
# curl http://127.0.0.1:5000/
