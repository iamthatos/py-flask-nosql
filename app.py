from flask import Flask
from flask_restful import Resource, Api


from db import db
from ma import ma
from model.task import Task
from schema.task import TaskSchema

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'mymongodb'
tasks_collection = TaskSchema(many=True)
api = Api(app)


class UsersResource(Resource):
    @classmethod
    def get(cls):
        return {'tasks': tasks_collection.dump(Task.find_all())}, 200


api.add_resource(UsersResource, '/api/task')


db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)