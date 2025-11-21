# Screenshot Submission Checklist

## Task 1: Repository and Kanban Board Setup (6 points)
- [ ] Screenshot: `planning-repository-done.jpg` - Repository with Kanban board setup
  - Should show: GitHub repository with README, file structure, and initial Kanban board

## Task 2: REST API Implementation (16 points)
- [ ] Screenshot: Setup and Kanban board showing Sprint 2 planning
- [ ] Screenshot: Kanban board with REST API user stories in progress/done
- [ ] Screenshot: Application URL showing the API is running
- [ ] Screenshot: REST API responses for:
  - GET /api/tasks
  - POST /api/tasks
  - GET /api/tasks/<id>
  - PUT /api/tasks/<id>
  - DELETE /api/tasks/<id>

## Task 3: CI/CD Pipeline (12 points)
- [ ] Screenshot: Sprint 2 Planning with CI/CD stories
- [ ] Screenshot: GitHub Actions badge showing build status
- [ ] Screenshot: GitHub Actions workflow run (ci-build.yaml execution)
- [ ] Screenshot: GitHub repository link showing ci-build.yaml file

## Task 4: Deployment (10 points)
- [ ] Screenshot: Sprint 3 Planning with deployment stories
- [ ] Screenshot: Kanban board showing deployment progress
- [ ] Screenshot: Docker image build/list output
- [ ] Screenshot: Application page running in browser
- [ ] Screenshot: Deployment details (Docker container info or hosting service)

## Task 5: Final Pipeline Run (6 points)
- [ ] Screenshot: Final Kanban board with all stories completed
- [ ] Screenshot: Log file from the CI/CD pipeline run

---

## Instructions for Taking Screenshots

### For Task 1 (planning-repository-done.jpg):
1. Go to your GitHub repository
2. Make sure README.md is visible
3. Show the file structure in the repository
4. Include the Projects/Kanban board tab
5. Save as `planning-repository-done.jpg`

### For Task 2 (REST API):
1. Open your Kanban board showing Sprint 2
2. Take screenshot of the board with API stories
3. Run the application: `python run.py`
4. Use browser or Postman to test API endpoints
5. Screenshot each API response

### For Task 3 (CI/CD):
1. Show Sprint 2 planning with CI/CD stories
2. Add GitHub Actions badge to README
3. Push code to trigger workflow
4. Screenshot the Actions tab showing green check
5. Screenshot the ci-build.yaml file content

### For Task 4 (Deployment):
1. Show Sprint 3 planning board
2. Build Docker image: `docker build -t kanban-app .`
3. Screenshot docker image list
4. Run container and show it in browser
5. Screenshot deployment details

### For Task 5 (Final):
1. Show completed Kanban board
2. Download/screenshot pipeline logs from GitHub Actions

---

## Screenshot File Naming Convention

All screenshots should be saved in the `screenshots/` directory with descriptive names:

- `planning-repository-done.jpg` (Required for Task 1a)
- `sprint2-planning.jpg`
- `sprint2-kanban-board.jpg`
- `api-url-running.jpg`
- `api-get-tasks.jpg`
- `api-post-task.jpg`
- `api-get-task-by-id.jpg`
- `api-put-task.jpg`
- `api-delete-task.jpg`
- `sprint2-cicd-planning.jpg`
- `github-actions-badge.jpg`
- `ci-workflow-run.jpg`
- `ci-build-yaml-file.jpg`
- `sprint3-planning.jpg`
- `sprint3-kanban-board.jpg`
- `docker-image.jpg`
- `application-page.jpg`
- `deployment-details.jpg`
- `final-kanban-board.jpg`
- `pipeline-logs.jpg`

---

## Tools for Testing REST API

### Using curl (Command Line):
```bash
# GET all tasks
curl http://localhost:5000/api/tasks

# POST new task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Task","description":"Testing API","status":"New"}'

# GET specific task
curl http://localhost:5000/api/tasks/1

# PUT update task
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"In Progress"}'

# DELETE task
curl -X DELETE http://localhost:5000/api/tasks/1
```

### Using Postman:
1. Download Postman
2. Create a new collection "Kanban API"
3. Add requests for each endpoint
4. Send requests and screenshot responses

### Using Browser:
- For GET requests, simply navigate to the URL
- For POST/PUT/DELETE, use browser developer tools or extensions

---

## Submission Format

When submitting to Coursera:
1. Organize all screenshots in order
2. Use clear, descriptive filenames
3. Ensure screenshots are high quality and readable
4. Include the GitHub repository URL in your submission
5. Verify all required screenshots are present before submitting
