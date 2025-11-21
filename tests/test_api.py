import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()

def test_index(client):
    """Test API root endpoint"""
    response = client.get('/api/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_get_tasks_empty(client):
    """Test getting tasks when database is empty"""
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['count'] == 0
    assert len(data['tasks']) == 0

def test_create_task(client):
    """Test creating a new task"""
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'status': 'New',
        'priority': 'High',
        'assigned_to': 'John Doe'
    }
    
    response = client.post('/api/tasks', json=task_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True
    assert data['task']['title'] == 'Test Task'
    assert data['task']['priority'] == 'High'

def test_create_task_without_title(client):
    """Test creating a task without title (should fail)"""
    task_data = {
        'description': 'This task has no title'
    }
    
    response = client.post('/api/tasks', json=task_data)
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False

def test_get_task_by_id(client):
    """Test getting a specific task by ID"""
    # First create a task
    task_data = {
        'title': 'Test Task for Get',
        'description': 'Testing get by ID'
    }
    create_response = client.post('/api/tasks', json=task_data)
    task_id = create_response.get_json()['task']['id']
    
    # Now get the task
    response = client.get(f'/api/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['task']['title'] == 'Test Task for Get'

def test_get_nonexistent_task(client):
    """Test getting a task that doesn't exist"""
    response = client.get('/api/tasks/9999')
    assert response.status_code == 404
    data = response.get_json()
    assert data['success'] is False

def test_update_task(client):
    """Test updating a task"""
    # Create a task
    task_data = {
        'title': 'Original Title',
        'status': 'New'
    }
    create_response = client.post('/api/tasks', json=task_data)
    task_id = create_response.get_json()['task']['id']
    
    # Update the task
    update_data = {
        'title': 'Updated Title',
        'status': 'In Progress'
    }
    response = client.put(f'/api/tasks/{task_id}', json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['task']['title'] == 'Updated Title'
    assert data['task']['status'] == 'In Progress'

def test_delete_task(client):
    """Test deleting a task"""
    # Create a task
    task_data = {
        'title': 'Task to Delete'
    }
    create_response = client.post('/api/tasks', json=task_data)
    task_id = create_response.get_json()['task']['id']
    
    # Delete the task
    response = client.delete(f'/api/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    
    # Verify task is deleted
    get_response = client.get(f'/api/tasks/{task_id}')
    assert get_response.status_code == 404

def test_filter_tasks_by_status(client):
    """Test filtering tasks by status"""
    # Create tasks with different statuses
    client.post('/api/tasks', json={'title': 'Task 1', 'status': 'New'})
    client.post('/api/tasks', json={'title': 'Task 2', 'status': 'In Progress'})
    client.post('/api/tasks', json={'title': 'Task 3', 'status': 'New'})
    
    # Filter by 'New' status
    response = client.get('/api/tasks?status=New')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 2
    assert all(task['status'] == 'New' for task in data['tasks'])
