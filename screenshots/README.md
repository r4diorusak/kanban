# Screenshots - README

This folder contains all screenshots required for the Coursera Peer-graded Assignment.

## Required Screenshots for Submission

### Task 1 (6 points):
1. `planning-repository-done.jpg` - Initial repository and Kanban board setup

### Task 2 (16 points):
2. `sprint2-planning.jpg` - Sprint 2 planning board
3. `sprint2-kanban-board.jpg` - Kanban board with API stories
4. `api-url-running.jpg` - Application running and accessible
5. `api-get-tasks.jpg` - GET all tasks response
6. `api-post-task.jpg` - POST create task response
7. `api-get-task-by-id.jpg` - GET specific task response
8. `api-put-task.jpg` - PUT update task response
9. `api-delete-task.jpg` - DELETE task response

### Task 3 (12 points):
10. `sprint2-cicd-planning.jpg` - Sprint 2 with CI/CD stories
11. `github-actions-badge.jpg` - GitHub Actions badge in README
12. `ci-workflow-run.jpg` - GitHub Actions workflow execution
13. `ci-build-yaml-file.jpg` - Contents of ci-build.yaml file

### Task 4 (10 points):
14. `sprint3-planning.jpg` - Sprint 3 planning
15. `sprint3-kanban-board.jpg` - Kanban board with deployment stories
16. `docker-image.jpg` - Docker image build output
17. `application-page.jpg` - Application running in browser
18. `deployment-details.jpg` - Docker container or deployment info

### Task 5 (6 points):
19. `final-kanban-board.jpg` - Completed Kanban board
20. `pipeline-logs.jpg` - CI/CD pipeline log file

---

## How to Capture These Screenshots

### Step 1: Set Up GitHub Repository
1. Create a new GitHub repository named "kanban"
2. Push all code to GitHub
3. Go to repository Settings → Enable Issues
4. Go to Projects → Create new project (Kanban board)
5. Take screenshot showing repository structure and Kanban board

### Step 2: Run and Test the Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py

# In another terminal, test API endpoints
curl http://localhost:5000/api/
curl http://localhost:5000/api/tasks
```

### Step 3: Set Up CI/CD
1. Push code with .github/workflows/ci-build.yaml
2. Go to Actions tab in GitHub
3. Watch the workflow run
4. Add badge to README

### Step 4: Docker Deployment
```bash
# Build Docker image
docker build -t kanban-app .

# Run container
docker run -p 5000:5000 kanban-app

# List images
docker images
```

---

## Tips for Good Screenshots
- Use high resolution (at least 1280x720)
- Ensure text is readable
- Capture entire relevant section
- Include browser address bar for URLs
- Show timestamps when relevant
- Highlight important information if needed

---

## File Naming Convention
- Use lowercase with hyphens
- Include task number or description
- Use .jpg or .png format
- Keep filenames consistent and descriptive
