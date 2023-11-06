from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

# Para testar
# curl http://localhost:5000/1 -d "data=Remember the milk" -X PUT
# curl http://localhost:5000/1
# curl http://localhost:5000/2 -d "data=Change my brakepads" -X PUT
# curl http://localhost:5000/2
