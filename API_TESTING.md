# API Testing Guide

This guide provides step-by-step instructions for testing all REST API endpoints and capturing screenshots for the assignment.

## Prerequisites

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:
   ```bash
   python run.py
   ```
   
   The application will run on `http://localhost:5000`

---

## API Endpoints Testing

### 1. Health Check
**Endpoint:** `GET /api/health`

**Command:**
```bash
curl http://localhost:5000/api/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

---

### 2. API Root
**Endpoint:** `GET /api/`

**Command:**
```bash
curl http://localhost:5000/api/
```

**Expected Response:**
```json
{
  "message": "Welcome to Kanban Board API",
  "version": "1.0",
  "endpoints": {
    "GET /api/tasks": "Get all tasks",
    "GET /api/tasks/<id>": "Get a specific task",
    "POST /api/tasks": "Create a new task",
    "PUT /api/tasks/<id>": "Update a task",
    "DELETE /api/tasks/<id>": "Delete a task"
  }
}
```

---

### 3. Get All Tasks
**Endpoint:** `GET /api/tasks`

**Command:**
```bash
curl http://localhost:5000/api/tasks
```

**Expected Response:**
```json
{
  "success": true,
  "count": 0,
  "tasks": []
}
```

**Screenshot Required:** Yes - `api-get-tasks.jpg`

---

### 4. Create a New Task
**Endpoint:** `POST /api/tasks`

**Command:**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implement user authentication",
    "description": "Add login and registration functionality",
    "status": "New",
    "priority": "High",
    "assigned_to": "John Doe"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Implement user authentication",
    "description": "Add login and registration functionality",
    "status": "New",
    "priority": "High",
    "assigned_to": "John Doe",
    "created_at": "2025-11-21T10:30:00",
    "updated_at": "2025-11-21T10:30:00"
  }
}
```

**Screenshot Required:** Yes - `api-post-task.jpg`

---

### 5. Get Specific Task
**Endpoint:** `GET /api/tasks/<id>`

**Command:**
```bash
curl http://localhost:5000/api/tasks/1
```

**Expected Response:**
```json
{
  "success": true,
  "task": {
    "id": 1,
    "title": "Implement user authentication",
    "description": "Add login and registration functionality",
    "status": "New",
    "priority": "High",
    "assigned_to": "John Doe",
    "created_at": "2025-11-21T10:30:00",
    "updated_at": "2025-11-21T10:30:00"
  }
}
```

**Screenshot Required:** Yes - `api-get-task-by-id.jpg`

---

### 6. Update a Task
**Endpoint:** `PUT /api/tasks/<id>`

**Command:**
```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress",
    "priority": "Medium"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Task updated successfully",
  "task": {
    "id": 1,
    "title": "Implement user authentication",
    "description": "Add login and registration functionality",
    "status": "In Progress",
    "priority": "Medium",
    "assigned_to": "John Doe",
    "created_at": "2025-11-21T10:30:00",
    "updated_at": "2025-11-21T10:35:00"
  }
}
```

**Screenshot Required:** Yes - `api-put-task.jpg`

---

### 7. Delete a Task
**Endpoint:** `DELETE /api/tasks/<id>`

**Command:**
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

**Screenshot Required:** Yes - `api-delete-task.jpg`

---

### 8. Filter Tasks by Status
**Endpoint:** `GET /api/tasks?status=<status>`

**Command:**
```bash
curl http://localhost:5000/api/tasks?status=New
```

**Expected Response:**
```json
{
  "success": true,
  "count": 2,
  "tasks": [
    {
      "id": 2,
      "title": "Task 1",
      "status": "New",
      ...
    },
    {
      "id": 3,
      "title": "Task 2",
      "status": "New",
      ...
    }
  ]
}
```

---

## Testing with Postman

### Import Collection

1. Open Postman
2. Click "Import"
3. Create requests for each endpoint:

**Collection Structure:**
```
Kanban API
├── Health Check (GET)
├── API Root (GET)
├── Get All Tasks (GET)
├── Create Task (POST)
├── Get Task by ID (GET)
├── Update Task (PUT)
├── Delete Task (DELETE)
└── Filter by Status (GET)
```

### Sample POST Request in Postman:
- Method: POST
- URL: `http://localhost:5000/api/tasks`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
  ```json
  {
    "title": "Design database schema",
    "description": "Create ER diagram and table structures",
    "status": "New",
    "priority": "High",
    "assigned_to": "Jane Smith"
  }
  ```

---

## Running Automated Tests

To run the automated test suite:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest --cov=app tests/

# Run specific test
pytest tests/test_api.py::test_create_task -v
```

**Expected Output:**
```
tests/test_api.py::test_index PASSED
tests/test_api.py::test_health_check PASSED
tests/test_api.py::test_get_tasks_empty PASSED
tests/test_api.py::test_create_task PASSED
tests/test_api.py::test_create_task_without_title PASSED
tests/test_api.py::test_get_task_by_id PASSED
tests/test_api.py::test_get_nonexistent_task PASSED
tests/test_api.py::test_update_task PASSED
tests/test_api.py::test_delete_task PASSED
tests/test_api.py::test_filter_tasks_by_status PASSED

====== 10 passed in 0.82s ======
```

---

## Sample Data for Testing

Create multiple tasks to populate your Kanban board:

```bash
# Task 1
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Set up development environment","status":"Done","priority":"High"}'

# Task 2
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Implement REST API","status":"Done","priority":"High"}'

# Task 3
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Write unit tests","status":"In Progress","priority":"High"}'

# Task 4
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Set up CI/CD pipeline","status":"In Progress","priority":"Medium"}'

# Task 5
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Create Docker image","status":"New","priority":"Medium"}'

# Task 6
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Deploy to production","status":"New","priority":"Low"}'
```

---

## Troubleshooting

### Issue: Connection Refused
**Solution:** Make sure the application is running: `python run.py`

### Issue: 404 Not Found
**Solution:** Check the endpoint URL is correct, including the `/api/` prefix

### Issue: 400 Bad Request
**Solution:** Verify JSON format and required fields (title is required)

### Issue: Database Error
**Solution:** Delete `kanban.db` file and restart the application to recreate the database

---

## Screenshots Checklist for Task 2

- [ ] Screenshot showing the application URL in browser
- [ ] Screenshot of GET /api/tasks response
- [ ] Screenshot of POST /api/tasks response (creating a task)
- [ ] Screenshot of GET /api/tasks/1 response (getting specific task)
- [ ] Screenshot of PUT /api/tasks/1 response (updating a task)
- [ ] Screenshot of DELETE /api/tasks/1 response (deleting a task)
- [ ] Screenshot of Kanban board showing the tasks in different columns
