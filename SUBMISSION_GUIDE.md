# Coursera Peer-Graded Assignment - Complete Submission Guide

## Assignment Overview
**Course:** Agile Development and DevOps  
**Assignment:** Final Project - Kanban Board Application  
**Total Points:** 50 points  
**Deadline:** November 25, 11:59 PM WIB

---

## Complete Task Breakdown

### Task 1: Repository and Kanban Board Setup (6 points)
✅ **Requirement:** Upload screenshot named `planning-repository-done.jpg`

**What to Include:**
- GitHub repository with proper structure
- README.md visible
- Kanban board with columns: New, In Progress, Done
- Initial user stories added to the board

**Steps to Complete:**
1. Create GitHub repository named "kanban"
2. Push all code to repository
3. Enable GitHub Projects/Issues
4. Create Kanban board with columns
5. Add user stories to the board
6. Take screenshot showing repository + board
7. Save as `planning-repository-done.jpg`

---

### Task 2: REST API Implementation (16 points)
✅ **Requirements:**
- Screenshot of Kanban board showing Sprint 2 planning
- Screenshot of setup and configuration
- Screenshot of application URL
- Screenshots of REST API responses for all endpoints

**What to Include:**
1. **Sprint 2 Kanban Board** - showing API user stories
2. **Application URL** - browser showing http://localhost:5000/api/
3. **API Responses:**
   - GET /api/tasks - Get all tasks
   - POST /api/tasks - Create new task
   - GET /api/tasks/<id> - Get specific task
   - PUT /api/tasks/<id> - Update task
   - DELETE /api/tasks/<id> - Delete task

**Steps to Complete:**
1. Move API stories to "In Progress" on Kanban board
2. Run application: `python run.py`
3. Test all API endpoints (see API_TESTING.md)
4. Screenshot each response
5. Move stories to "Done" on Kanban board
6. Screenshot final board state

**Files to Reference:**
- `API_TESTING.md` - Complete API testing guide
- `app/routes.py` - API implementation

---

### Task 3: CI/CD Pipeline (12 points)
✅ **Requirements:**
- Screenshot of Sprint 2 Planning with CI/CD stories
- Screenshot of GitHub Actions badge
- Screenshot of ci-workflow run
- GitHub repo link showing ci-build.yaml file

**What to Include:**
1. **Sprint 2 Planning** - CI/CD user stories on board
2. **GitHub Actions Badge** - Build status badge in README
3. **Workflow Run** - Actions tab showing successful run
4. **ci-build.yaml** - File contents in repository

**Steps to Complete:**
1. Add CI/CD stories to Kanban board
2. Push code to GitHub (triggers workflow)
3. Go to Actions tab, wait for completion
4. Add badge to README: `![CI Build](https://github.com/USERNAME/kanban/actions/workflows/ci-build.yaml/badge.svg)`
5. Screenshot Actions tab showing green check
6. Screenshot ci-build.yaml file in repository
7. Move CI/CD stories to "Done"

**Files to Reference:**
- `.github/workflows/ci-build.yaml` - CI/CD configuration
- `tests/test_api.py` - Automated tests

---

### Task 4: Deployment (10 points)
✅ **Requirements:**
- Screenshot of Sprint 3 Planning
- Screenshot of Kanban board with deployment stories
- Screenshot of Docker image
- Screenshot of application page
- Screenshot of deployment details

**What to Include:**
1. **Sprint 3 Planning** - Deployment stories on board
2. **Docker Image** - Output of `docker images`
3. **Application Running** - Browser showing deployed app
4. **Deployment Details** - Docker container info or hosting service dashboard

**Steps to Complete:**
1. Add deployment stories to board
2. Build Docker image: `docker build -t kanban-app .`
3. Screenshot `docker images` output
4. Run container: `docker run -p 5000:5000 kanban-app`
5. Screenshot `docker ps` output
6. Open browser to http://localhost:5000/api/
7. Screenshot application page
8. Screenshot deployment platform (if using cloud)
9. Move deployment stories to "Done"

**Files to Reference:**
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose setup
- `DEPLOYMENT.md` - Complete deployment guide

---

### Task 5: Final Pipeline Run (6 points)
✅ **Requirements:**
- Screenshot of final Kanban board
- Log file of pipeline run

**What to Include:**
1. **Final Kanban Board** - All stories in "Done" column
2. **Pipeline Logs** - CI/CD workflow execution logs

**Steps to Complete:**
1. Ensure all stories are moved to "Done"
2. Screenshot complete Kanban board
3. Go to GitHub Actions tab
4. Click on latest workflow run
5. Screenshot or download logs
6. Save as `pipeline-logs.jpg` or `pipeline-logs.txt`

---

## File Structure for Submission

```
screenshots/
├── planning-repository-done.jpg           # Task 1
├── sprint2-planning.jpg                   # Task 2
├── sprint2-kanban-board.jpg              # Task 2
├── api-url-running.jpg                    # Task 2
├── api-get-tasks.jpg                      # Task 2
├── api-post-task.jpg                      # Task 2
├── api-get-task-by-id.jpg                # Task 2
├── api-put-task.jpg                       # Task 2
├── api-delete-task.jpg                    # Task 2
├── sprint2-cicd-planning.jpg             # Task 3
├── github-actions-badge.jpg              # Task 3
├── ci-workflow-run.jpg                    # Task 3
├── ci-build-yaml-file.jpg                # Task 3
├── sprint3-planning.jpg                   # Task 4
├── sprint3-kanban-board.jpg              # Task 4
├── docker-image.jpg                       # Task 4
├── application-page.jpg                   # Task 4
├── deployment-details.jpg                 # Task 4
├── final-kanban-board.jpg                # Task 5
└── pipeline-logs.jpg                      # Task 5
```

---

## Quick Start Commands

### 1. Setup Project
```bash
cd d:\Documents\GitHub\Coursera\kanban

# Install dependencies
pip install -r requirements.txt

# Run application
python run.py
```

### 2. Test API
```bash
# In another terminal
curl http://localhost:5000/api/health
curl http://localhost:5000/api/tasks
```

### 3. Run Tests
```bash
pytest tests/ -v
pytest --cov=app tests/
```

### 4. Docker
```bash
# Build
docker build -t kanban-app .

# Run
docker run -p 5000:5000 kanban-app

# Or use Docker Compose
docker-compose up -d
```

### 5. Git Commands
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit: Kanban board application"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/kanban.git
git push -u origin main
```

---

## Kanban Board Setup Guide

### Using GitHub Projects (Built-in)

1. **Create Project:**
   - Go to your repository
   - Click "Projects" tab
   - Click "New project"
   - Choose "Board" template
   - Name it "Kanban Board"

2. **Create Columns:**
   - Rename columns to: New, In Progress, Done
   - Drag and drop to reorder

3. **Add User Stories:**
   - Click "+ Add item" under each column
   - Copy user stories from `KANBAN_PLANNING.md`
   - Assign to yourself
   - Add labels (Sprint 1, Sprint 2, Sprint 3)

4. **User Stories to Add:**
   - Sprint 1: Setup and Planning (5 stories)
   - Sprint 2: REST API + CI/CD (4 stories)
   - Sprint 3: Deployment (2 stories)

### Alternative: ZenHub

If using ZenHub:
1. Install ZenHub browser extension
2. Go to your GitHub repository
3. Click "Boards" tab
4. Create columns: New, In Progress, Review, Done
5. Add issues as cards

---

## Screenshot Quality Guidelines

### Technical Requirements:
- **Resolution:** Minimum 1280x720
- **Format:** JPG or PNG
- **Size:** Less than 5MB per image
- **Clarity:** Text must be readable

### What to Show:
- **Full context:** Include browser address bar
- **Timestamps:** When relevant
- **Status indicators:** Green checkmarks, build badges
- **Code snippets:** Readable font size
- **Annotations:** Highlight important parts if needed

### Tools for Screenshots:
- **Windows:** Snipping Tool, Snip & Sketch (Win + Shift + S)
- **Browser Extensions:** Awesome Screenshot, Nimbus
- **Full Page:** Use browser dev tools (Ctrl + Shift + P → "Capture full size screenshot")

---

## Submission Process

### On Coursera:

1. **Go to Assignment Page**
2. **Upload Screenshots:**
   - Can upload multiple files
   - Or create a single document with all screenshots
   - Or provide Google Drive/Dropbox link

3. **Include GitHub Repository URL:**
   ```
   https://github.com/YOUR_USERNAME/kanban
   ```

4. **Add Description:**
   - Brief explanation of each task
   - Challenges faced and solutions
   - Technologies used

5. **Submit for Review**

---

## Peer Review Criteria

When grading peers, check:

### Task 1 (6 pts):
- [ ] Repository exists and is accessible
- [ ] README.md is present and informative
- [ ] Kanban board is set up with proper columns
- [ ] Screenshot shows clear evidence of planning phase

### Task 2 (16 pts):
- [ ] All 5 REST API endpoints are implemented
- [ ] Screenshots show successful API responses
- [ ] Application URL is visible and accessible
- [ ] Kanban board shows API stories completed

### Task 3 (12 pts):
- [ ] CI/CD workflow file (ci-build.yaml) exists
- [ ] GitHub Actions badge is present
- [ ] Workflow runs successfully (green check)
- [ ] Tests are automated and passing

### Task 4 (10 pts):
- [ ] Docker image is built successfully
- [ ] Application runs in container
- [ ] Deployment is functional
- [ ] Screenshots show all components

### Task 5 (6 pts):
- [ ] Final Kanban board shows all work complete
- [ ] Pipeline logs are provided
- [ ] All acceptance criteria met

---

## Common Issues and Solutions

### Issue 1: Port Already in Use
**Solution:**
```bash
# Windows PowerShell
Get-Process -Id (Get-NetTCPConnection -LocalPort 5000).OwningProcess | Stop-Process -Force
```

### Issue 2: Module Not Found
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 3: Database Errors
**Solution:**
```bash
# Delete and recreate database
rm kanban.db
python run.py
```

### Issue 4: GitHub Actions Failing
**Solution:**
- Check ci-build.yaml syntax
- Ensure all tests pass locally first
- Check GitHub Actions logs for details

### Issue 5: Docker Build Fails
**Solution:**
```bash
# Clear Docker cache
docker system prune -a
docker build --no-cache -t kanban-app .
```

---

## Additional Resources

### Documentation Files:
- `README.md` - Project overview
- `KANBAN_PLANNING.md` - Sprint planning and user stories
- `API_TESTING.md` - API endpoint testing guide
- `DEPLOYMENT.md` - Deployment instructions
- `SCREENSHOT_CHECKLIST.md` - Screenshot requirements

### Code Files:
- `app/` - Application code
- `tests/` - Automated tests
- `.github/workflows/` - CI/CD configuration
- `Dockerfile` - Container configuration

---

## Final Checklist

Before submission, verify:

- [ ] All code is pushed to GitHub
- [ ] GitHub repository is public
- [ ] README.md is complete with badges
- [ ] All 20+ screenshots are captured
- [ ] Screenshots are properly named
- [ ] All tests are passing
- [ ] CI/CD pipeline is green
- [ ] Docker image builds successfully
- [ ] Application runs locally
- [ ] API endpoints work correctly
- [ ] Kanban board shows all completed work
- [ ] GitHub repository URL is noted
- [ ] Submission deadline is met (Nov 25, 11:59 PM WIB)

---

## Grading Rubric Summary

| Task | Points | Key Deliverables |
|------|--------|------------------|
| Task 1 | 6 | Repository + Kanban board screenshot |
| Task 2 | 16 | REST API implementation + screenshots |
| Task 3 | 12 | CI/CD pipeline + workflow screenshots |
| Task 4 | 10 | Docker deployment + screenshots |
| Task 5 | 6 | Final board + pipeline logs |
| **Total** | **50** | **Complete project with documentation** |

---

## Time Estimate

- **Task 1:** 30-60 minutes (setup)
- **Task 2:** 2-3 hours (development + testing)
- **Task 3:** 1-2 hours (CI/CD setup)
- **Task 4:** 1-2 hours (Docker + deployment)
- **Task 5:** 30 minutes (final screenshots)
- **Total:** 5-8 hours

---

## Contact and Support

If you encounter issues:
1. Review documentation files in the repository
2. Check GitHub Actions logs for CI/CD issues
3. Test locally before screenshotting
4. Use Coursera discussion forums for help
5. Reference the course materials

---

## Good Luck! 🚀

Remember:
- Start early to avoid last-minute issues
- Test everything before taking screenshots
- Keep your repository clean and organized
- Document your work thoroughly
- Help your peers in review
