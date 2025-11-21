"""
Test all API endpoints manually
This script tests all REST API endpoints and displays results
Useful for taking screenshots for Task 2
"""

import requests
import json
from time import sleep

BASE_URL = "http://localhost:5000/api"

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)

def print_response(response):
    """Print formatted response"""
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response:")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)

def test_health_check():
    """Test health check endpoint"""
    print_header("TEST 1: Health Check")
    print(f"GET {BASE_URL}/health")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_api_root():
    """Test API root endpoint"""
    print_header("TEST 2: API Root")
    print(f"GET {BASE_URL}/")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_get_all_tasks():
    """Test get all tasks endpoint"""
    print_header("TEST 3: Get All Tasks")
    print(f"GET {BASE_URL}/tasks")
    
    try:
        response = requests.get(f"{BASE_URL}/tasks")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_create_task():
    """Test create task endpoint"""
    print_header("TEST 4: Create New Task")
    
    task_data = {
        "title": "Implement user authentication",
        "description": "Add login and registration functionality with JWT tokens",
        "status": "New",
        "priority": "High",
        "assigned_to": "John Doe"
    }
    
    print(f"POST {BASE_URL}/tasks")
    print(f"Request Body:")
    print(json.dumps(task_data, indent=2))
    
    try:
        response = requests.post(
            f"{BASE_URL}/tasks",
            json=task_data,
            headers={"Content-Type": "application/json"}
        )
        print_response(response)
        
        if response.status_code == 201:
            return response.json().get('task', {}).get('id')
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def test_get_task_by_id(task_id):
    """Test get task by ID endpoint"""
    print_header(f"TEST 5: Get Task by ID (ID: {task_id})")
    print(f"GET {BASE_URL}/tasks/{task_id}")
    
    try:
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_update_task(task_id):
    """Test update task endpoint"""
    print_header(f"TEST 6: Update Task (ID: {task_id})")
    
    update_data = {
        "status": "In Progress",
        "priority": "Medium",
        "description": "Updated: Add login and registration functionality with JWT tokens and password hashing"
    }
    
    print(f"PUT {BASE_URL}/tasks/{task_id}")
    print(f"Request Body:")
    print(json.dumps(update_data, indent=2))
    
    try:
        response = requests.put(
            f"{BASE_URL}/tasks/{task_id}",
            json=update_data,
            headers={"Content-Type": "application/json"}
        )
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_filter_tasks():
    """Test filter tasks by status"""
    print_header("TEST 7: Filter Tasks by Status")
    
    statuses = ["New", "In Progress", "Done"]
    
    for status in statuses:
        print(f"\nGET {BASE_URL}/tasks?status={status}")
        try:
            response = requests.get(f"{BASE_URL}/tasks?status={status}")
            print_response(response)
            sleep(0.5)
        except Exception as e:
            print(f"ERROR: {e}")

def test_delete_task(task_id):
    """Test delete task endpoint"""
    print_header(f"TEST 8: Delete Task (ID: {task_id})")
    print(f"DELETE {BASE_URL}/tasks/{task_id}")
    
    try:
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_get_nonexistent_task():
    """Test getting a task that doesn't exist"""
    print_header("TEST 9: Get Non-existent Task (Error Handling)")
    print(f"GET {BASE_URL}/tasks/9999")
    
    try:
        response = requests.get(f"{BASE_URL}/tasks/9999")
        print_response(response)
        return response.status_code == 404
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def create_sample_tasks():
    """Create multiple sample tasks for testing"""
    print_header("Creating Sample Tasks for Kanban Board")
    
    sample_tasks = [
        {
            "title": "Set up development environment",
            "description": "Install Python, Docker, and required tools",
            "status": "Done",
            "priority": "High",
            "assigned_to": "Development Team"
        },
        {
            "title": "Implement REST API",
            "description": "Create all CRUD endpoints for tasks",
            "status": "Done",
            "priority": "High",
            "assigned_to": "Backend Developer"
        },
        {
            "title": "Write unit tests",
            "description": "Test all API endpoints with pytest",
            "status": "In Progress",
            "priority": "High",
            "assigned_to": "QA Engineer"
        },
        {
            "title": "Set up CI/CD pipeline",
            "description": "Configure GitHub Actions workflow",
            "status": "In Progress",
            "priority": "Medium",
            "assigned_to": "DevOps Engineer"
        },
        {
            "title": "Create Docker image",
            "description": "Containerize the application",
            "status": "New",
            "priority": "Medium",
            "assigned_to": "DevOps Engineer"
        },
        {
            "title": "Deploy to production",
            "description": "Deploy application to hosting platform",
            "status": "New",
            "priority": "Low",
            "assigned_to": "DevOps Team"
        }
    ]
    
    created_ids = []
    for task in sample_tasks:
        try:
            response = requests.post(
                f"{BASE_URL}/tasks",
                json=task,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 201:
                task_id = response.json().get('task', {}).get('id')
                created_ids.append(task_id)
                print(f"✓ Created: {task['title']} (ID: {task_id})")
            sleep(0.3)
        except Exception as e:
            print(f"✗ Failed to create: {task['title']} - {e}")
    
    print(f"\nCreated {len(created_ids)} sample tasks")
    return created_ids

def run_all_tests():
    """Run all API tests"""
    print("\n" + "="*70)
    print("  KANBAN API - COMPREHENSIVE TEST SUITE")
    print("  Make sure the application is running: python run.py")
    print("="*70)
    
    # Check if API is accessible
    try:
        requests.get(BASE_URL, timeout=2)
    except:
        print("\n❌ ERROR: Cannot connect to API")
        print("   Please ensure the application is running on http://localhost:5000")
        print("   Run: python run.py")
        return
    
    results = []
    
    # Test 1: Health Check
    results.append(("Health Check", test_health_check()))
    sleep(0.5)
    
    # Test 2: API Root
    results.append(("API Root", test_api_root()))
    sleep(0.5)
    
    # Test 3: Get All Tasks (initially empty or with existing data)
    results.append(("Get All Tasks", test_get_all_tasks()))
    sleep(0.5)
    
    # Test 4: Create Task
    task_id = test_create_task()
    results.append(("Create Task", task_id is not None))
    sleep(0.5)
    
    if task_id:
        # Test 5: Get Task by ID
        results.append(("Get Task by ID", test_get_task_by_id(task_id)))
        sleep(0.5)
        
        # Test 6: Update Task
        results.append(("Update Task", test_update_task(task_id)))
        sleep(0.5)
        
        # Test 7: Filter Tasks
        test_filter_tasks()
        sleep(0.5)
        
        # Test 8: Delete Task
        results.append(("Delete Task", test_delete_task(task_id)))
        sleep(0.5)
    
    # Test 9: Error Handling
    results.append(("Error Handling", test_get_nonexistent_task()))
    sleep(0.5)
    
    # Create sample tasks
    print_header("Creating Sample Tasks")
    sample_ids = create_sample_tasks()
    sleep(0.5)
    
    # Show final state
    print_header("Final State: All Tasks")
    test_get_all_tasks()
    
    # Print summary
    print_header("TEST SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nTests Passed: {passed}/{total}")
    print("\nDetailed Results:")
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - {test_name}")
    
    if sample_ids:
        print(f"\nSample Tasks Created: {len(sample_ids)}")
        print("Task IDs:", sample_ids)
    
    print("\n" + "="*70)
    print("  Testing Complete!")
    print("  Use these results for your Task 2 screenshots")
    print("="*70 + "\n")

if __name__ == '__main__':
    run_all_tests()
