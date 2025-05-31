from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'description': t.description, 'completed': t.completed} for t in tasks])

@task_bp.route('/', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(task)
    db.session.commit()
    return jsonify(message="Task created"), 201
