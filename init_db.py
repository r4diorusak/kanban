"""
Initialize database with sample data for testing
Run this script to populate the database with sample tasks
"""

from app import create_app, db
from app.models import Task

def init_db():
    """Initialize database with sample tasks"""
    app = create_app()
    
    with app.app_context():
        # Drop all tables and recreate
        print("Dropping existing tables...")
        db.drop_all()
        
        print("Creating new tables...")
        db.create_all()
        
        # Sample tasks for Sprint 1
        sprint1_tasks = [
            Task(
                title="Set up GitHub repository",
                description="Create GitHub repository and push initial code",
                status="Done",
                priority="High",
                assigned_to="Development Team"
            ),
            Task(
                title="Create project documentation",
                description="Write README and documentation files",
                status="Done",
                priority="High",
                assigned_to="Development Team"
            ),
            Task(
                title="Define user stories",
                description="Create and prioritize user stories for all sprints",
                status="Done",
                priority="High",
                assigned_to="Product Owner"
            ),
            Task(
                title="Set up Kanban board",
                description="Configure Kanban board with columns and labels",
                status="Done",
                priority="Medium",
                assigned_to="Scrum Master"
            ),
        ]
        
        # Sample tasks for Sprint 2
        sprint2_tasks = [
            Task(
                title="Implement REST API endpoints",
                description="Create GET, POST, PUT, DELETE endpoints for tasks",
                status="Done",
                priority="High",
                assigned_to="Backend Developer"
            ),
            Task(
                title="Add task filtering",
                description="Implement status-based filtering for tasks",
                status="Done",
                priority="Medium",
                assigned_to="Backend Developer"
            ),
            Task(
                title="Write unit tests",
                description="Create comprehensive unit tests for all API endpoints",
                status="In Progress",
                priority="High",
                assigned_to="QA Engineer"
            ),
            Task(
                title="Set up CI/CD pipeline",
                description="Configure GitHub Actions for automated testing",
                status="In Progress",
                priority="High",
                assigned_to="DevOps Engineer"
            ),
        ]
        
        # Sample tasks for Sprint 3
        sprint3_tasks = [
            Task(
                title="Create Dockerfile",
                description="Write Dockerfile for containerizing the application",
                status="New",
                priority="High",
                assigned_to="DevOps Engineer"
            ),
            Task(
                title="Build Docker image",
                description="Build and test Docker image locally",
                status="New",
                priority="High",
                assigned_to="DevOps Engineer"
            ),
            Task(
                title="Deploy to production",
                description="Deploy application to hosting platform",
                status="New",
                priority="Medium",
                assigned_to="DevOps Engineer"
            ),
            Task(
                title="Configure monitoring",
                description="Set up application monitoring and health checks",
                status="New",
                priority="Low",
                assigned_to="DevOps Engineer"
            ),
        ]
        
        # Add all tasks to database
        print("\nAdding sample tasks...")
        all_tasks = sprint1_tasks + sprint2_tasks + sprint3_tasks
        
        for task in all_tasks:
            db.session.add(task)
            print(f"  - Added: {task.title} [{task.status}]")
        
        # Commit changes
        db.session.commit()
        
        # Display summary
        print("\n" + "="*60)
        print("Database initialized successfully!")
        print("="*60)
        print(f"\nTotal tasks created: {len(all_tasks)}")
        print(f"  - Done: {len([t for t in all_tasks if t.status == 'Done'])}")
        print(f"  - In Progress: {len([t for t in all_tasks if t.status == 'In Progress'])}")
        print(f"  - New: {len([t for t in all_tasks if t.status == 'New'])}")
        print("\nRun 'python run.py' to start the application")
        print("Then visit http://localhost:5000/api/tasks to see the tasks")
        print("="*60 + "\n")

if __name__ == '__main__':
    init_db()
