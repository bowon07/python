from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Task API',
    description='A simple Task API',
)

ns = api.namespace('tasks', description='Task operations')

task = api.model('Task', {
    'name': fields.String(required=True, description='The task name'),
    'description': fields.String(required=True, description='The task description')
})

TASKS = {}  # 데이터를 저장할 간단한 딕셔너리

@ns.route('/')
class TaskList(Resource):
    @ns.doc('list_tasks')
    def get(self):
        """모든 task를 가져옵니다."""
        return TASKS

    @ns.doc('create_task')
    @ns.expect(task)
    @ns.marshal_with(task, code=201)
    def post(self):
        """새로운 task를 생성합니다."""
        id = len(TASKS) + 1
        TASKS[id] = api.payload
        return TASKS[id], 201

@ns.route('/<int:id>')
@ns.response(404, 'Task not found')
@ns.param('id', 'The task identifier')
class Task(Resource):
    @ns.doc('get_task')
    def get(self, id):
        """특정 task를 가져옵니다."""
        return {id: TASKS[id]}

    @ns.doc('delete_task')
    @ns.response(204, 'Task deleted')
    def delete(self, id):
        """특정 task를 삭제합니다."""
        del TASKS[id]
        return '', 204

    @ns.expect(task)
    @ns.marshal_with(task)
    def put(self, id):
        """특정 task를 수정합니다."""
        TASKS[id] = api.payload
        return {id: TASKS[id]}

if __name__ == '__main__':
    app.run(debug=True)
