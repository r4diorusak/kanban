from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

api = Blueprint('api', __name__)

@api.route('/')
def index():
    """API root endpoint"""
    return jsonify({
        'message': 'Welcome to Kanban Board API',
        'version': '1.0',
        'endpoints': {
            'GET /api/tasks': 'Get all tasks',
            'GET /api/tasks/<id>': 'Get a specific task',
            'POST /api/tasks': 'Create a new task',
            'PUT /api/tasks/<id>': 'Update a task',
            'DELETE /api/tasks/<id>': 'Delete a task'
        }
    })

@api.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    })

@api.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        status_filter = request.args.get('status')
        
        if status_filter:
            tasks = Task.query.filter_by(status=status_filter).all()
        else:
            tasks = Task.query.all()
        
        return jsonify({
            'success': True,
            'count': len(tasks),
            'tasks': [task.to_dict() for task in tasks]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    try:
        task = Task.query.get(task_id)
        
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        return jsonify({
            'success': True,
            'task': task.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        
        if not data or 'title' not in data:
            return jsonify({
                'success': False,
                'error': 'Title is required'
            }), 400
        
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', 'New'),
            priority=data.get('priority', 'Medium'),
            assigned_to=data.get('assigned_to', '')
        )
        
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Task created successfully',
            'task': task.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    try:
        task = Task.query.get(task_id)
        
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        data = request.get_json()
        
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'status' in data:
            task.status = data['status']
        if 'priority' in data:
            task.priority = data['priority']
        if 'assigned_to' in data:
            task.assigned_to = data['assigned_to']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Task updated successfully',
            'task': task.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        task = Task.query.get(task_id)
        
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    }), 200
