# Final Project Submission Checklist
**Total Points: 50**

---

## Task 1: Repository and Kanban Board Screenshots (6 pts)

### Required Screenshots:
- [ ] `planning-repository-done.jpg`
  - Show: GitHub repository homepage
  - Show: File structure visible (README.md, app/, tests/, etc.)
  - Show: Kanban board tab or Projects section
  - Show: Initial setup complete

- [ ] `planning-userstories-done.jpg`
  - Show: Kanban board with all columns (Todo, In Progress, Done)
  - Show: User stories in Done column (completed items)
  - Show: Clear visibility of task titles and status

**What to capture:**
1. Navigate to: https://github.com/r4diorusak/kanban
2. Show repository structure
3. Show Projects/Kanban board
4. Ensure Done column shows completed user stories

---

## Task 2: REST API Implementation (16 pts)

### Required Screenshots:

- [ ] `sprint2-planning.jpg`
  - Show: Kanban board with Sprint 2 user stories
  - Show: REST API related tasks (CRUD operations)
  - Show: Tasks in different status columns

- [ ] `api-running.jpg`
  - Show: Terminal with `python run.py` running
  - Show: Flask application started
  - Show: URL where API is accessible (e.g., http://localhost:5000)

- [ ] `api-get-tasks.jpg`
  - Show: Browser or Postman with GET /api/tasks request
  - Show: Response with JSON data (list of tasks)
  - Show: HTTP 200 status

- [ ] `api-post-task.jpg`
  - Show: POST /api/tasks request
  - Show: Request body with new task data
  - Show: Response with created task (HTTP 201)

- [ ] `api-get-task-id.jpg`
  - Show: GET /api/tasks/<id> request
  - Show: Single task response
  - Show: HTTP 200 status

- [ ] `api-put-task.jpg`
  - Show: PUT /api/tasks/<id> request
  - Show: Request body with updated data
  - Show: Response with updated task

- [ ] `api-delete-task.jpg`
  - Show: DELETE /api/tasks/<id> request
  - Show: Success response
  - Show: HTTP 200/204 status

**What to do:**
1. Implement REST API endpoints in `app/routes.py`
2. Test each endpoint using browser/Postman
3. Screenshot each API response

---

## Task 3: CI/CD Pipeline (12 pts)

### Required Screenshots:

- [ ] `sprint2-cicd-planning.jpg`
  - Show: Kanban board with CI/CD user stories
  - Show: GitHub Actions setup tasks
  - Show: Testing and automation stories

- [ ] `github-actions-badge.jpg`
  - Show: README.md with GitHub Actions badge
  - Show: Badge status (passing/failing)
  - Show: Build status visible

- [ ] `github-actions-workflow.jpg`
  - Show: GitHub Actions tab
  - Show: Workflow run details
  - Show: All steps completed successfully
  - Show: Test results

- [ ] `ci-build-yaml.jpg`
  - Show: GitHub repository file view
  - Show: `.github/workflows/ci-build.yaml` file
  - Show: Workflow configuration visible

**What to do:**
1. Create `.github/workflows/ci-build.yaml`
2. Configure automated testing
3. Push changes to trigger workflow
4. Screenshot workflow results

---

## Task 4: Deployment (10 pts)

### Required Screenshots:

- [ ] `sprint3-planning.jpg`
  - Show: Kanban board with Sprint 3 deployment stories
  - Show: Docker and deployment related tasks
  - Show: Tasks distribution across columns

- [ ] `deployment-progress.jpg`
  - Show: Kanban board during deployment
  - Show: Tasks moving to Done
  - Show: Deployment completion status

- [ ] `docker-image.jpg`
  - Show: Terminal with `docker images` command
  - Show: Built Docker image listed
  - Show: Image size and tag

- [ ] `application-deployed.jpg`
  - Show: Browser with deployed application URL
  - Show: Application running (homepage or API response)
  - Show: Production URL visible

- [ ] `deployment-details.jpg`
  - Show: Docker container info (`docker ps`) OR
  - Show: Hosting platform dashboard (Render/Railway/etc.)
  - Show: Deployment configuration/logs

**What to do:**
1. Create Dockerfile
2. Build Docker image: `docker build -t kanban-app .`
3. Deploy to hosting platform (Render, Railway, etc.)
4. Verify application is accessible
5. Screenshot deployment details

---

## Task 5: Final Pipeline and Completion (6 pts)

### Required Screenshots:

- [ ] `final-kanban-board.jpg`
  - Show: Complete Kanban board
  - Show: All user stories in Done column
  - Show: Project completion status
  - Show: All sprints completed

- [ ] `pipeline-log.jpg`
  - Show: Final CI/CD pipeline run
  - Show: All tests passing
  - Show: Deployment successful
  - Show: Complete log output

**What to do:**
1. Ensure all tasks are completed
2. Run final CI/CD pipeline
3. Screenshot final board state
4. Capture complete pipeline logs

---

## Submission Guidelines

### File Naming Convention:
- Use exact names as specified above
- Format: `.jpg` (JPEG image files)
- Location: `screenshots/` folder
- Lowercase with hyphens

### Screenshot Requirements:
- **Clear and readable** text
- **Full context** visible
- **No sensitive information** (tokens, passwords)
- **Proper zoom level** - not too zoomed in/out
- **Date/timestamp** visible where relevant

### Quality Checklist:
- [ ] All screenshots are in JPG format
- [ ] File names match exactly as specified
- [ ] All required elements are visible
- [ ] Screenshots are clear and high resolution
- [ ] No personal/sensitive data exposed
- [ ] All files uploaded to GitHub repository

---

## Current Progress Tracking

### Completed:
- [x] Repository setup
- [x] README documentation
- [x] User stories defined
- [x] Kanban board configured
- [x] Python project initialized

### In Progress:
- [ ] REST API implementation
- [ ] Unit tests
- [ ] CI/CD pipeline
- [ ] Docker containerization

### Todo:
- [ ] Deployment
- [ ] Final testing
- [ ] Screenshot collection
- [ ] Peer review submission

---

## Grading Breakdown

| Task | Points | Description |
|------|--------|-------------|
| Task 1 | 6 pts | Repository & Kanban Board |
| Task 2 | 16 pts | REST API Implementation |
| Task 3 | 12 pts | CI/CD Pipeline |
| Task 4 | 10 pts | Deployment |
| Task 5 | 6 pts | Final Completion |
| **Total** | **50 pts** | **Final Project** |

---

**Note:** This is a peer-reviewed assignment. Ensure all screenshots clearly demonstrate the completed work as your peers will be evaluating based on these submissions.

**Repository:** https://github.com/r4diorusak/kanban  
**Last Updated:** November 21, 2025
