"""Script to add sample data to the database"""
from app import create_app, db
from app.models import Task

app = create_app()

with app.app_context():
    # Clear existing data
    Task.query.delete()
    
    # Add sample tasks
    tasks = [
        Task(
            title="Set up GitHub repository",
            description="Create repository and initialize project structure",
            status="Done",
            priority="High"
        ),
        Task(
            title="Implement REST API",
            description="Create CRUD endpoints for task management",
            status="In Progress",
            priority="High"
        ),
        Task(
            title="Write unit tests",
            description="Create test cases for all API endpoints",
            status="In Progress",
            priority="Medium"
        ),
        Task(
            title="Setup CI/CD pipeline",
            description="Configure GitHub Actions for automated testing",
            status="New",
            priority="Medium"
        ),
        Task(
            title="Deploy to production",
            description="Deploy application to cloud hosting",
            status="New",
            priority="Low"
        )
    ]
    
    for task in tasks:
        db.session.add(task)
    
    db.session.commit()
    print(f"✓ Added {len(tasks)} sample tasks to database")
