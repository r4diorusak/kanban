# 🚀 Getting Started - Step by Step Guide

This guide will walk you through setting up and running the Kanban Board application from scratch.

## 📋 Prerequisites Checklist

Before you begin, make sure you have:

- [ ] Windows PC (you're already on Windows)
- [ ] Python 3.9+ installed
- [ ] Git installed
- [ ] GitHub account
- [ ] Text editor (VS Code recommended)
- [ ] PowerShell terminal
- [ ] Docker Desktop (optional, for Task 4)
- [ ] Internet connection

### Check Your Setup

Open PowerShell and run these commands to verify:

```powershell
# Check Python version (should be 3.9+)
python --version

# Check pip
pip --version

# Check Git
git --version

# Check Docker (optional)
docker --version
```

---

## 🎯 Step-by-Step Walkthrough

### Phase 1: Project Setup (15 minutes)

#### Step 1: Navigate to Project Directory

```powershell
cd d:\Documents\GitHub\Coursera\kanban
```

#### Step 2: Verify Project Files

```powershell
# List all files
ls

# You should see these files:
# - README.md
# - requirements.txt
# - run.py
# - Dockerfile
# - etc.
```

#### Step 3: Install Python Dependencies

```powershell
# Install all required packages
pip install -r requirements.txt

# This will install:
# - Flask (web framework)
# - SQLAlchemy (database)
# - pytest (testing)
# - requests (API testing)
# - and more...
```

**Expected Output:**
```
Successfully installed Flask-3.0.0 Flask-SQLAlchemy-3.1.1 ...
```

#### Step 4: Initialize Database with Sample Data

```powershell
# Run the database initialization script
python init_db.py
```

**Expected Output:**
```
Dropping existing tables...
Creating new tables...
Adding sample tasks...
  - Added: Set up GitHub repository [Done]
  - Added: Create project documentation [Done]
  ...
Database initialized successfully!
Total tasks created: 12
```

#### Step 5: Run the Application

```powershell
# Start the Flask application
python run.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

**✅ Success!** Your application is now running at http://localhost:5000

---

### Phase 2: Test the Application (10 minutes)

#### Step 6: Open a New PowerShell Terminal

Keep the application running in the first terminal, and open a new one.

```powershell
cd d:\Documents\GitHub\Coursera\kanban
```

#### Step 7: Test API with curl

```powershell
# Test health check
curl http://localhost:5000/api/health

# Get all tasks
curl http://localhost:5000/api/tasks

# Get API information
curl http://localhost:5000/api/
```

**Alternative:** Open browser and visit:
- http://localhost:5000/api/
- http://localhost:5000/api/tasks
- http://localhost:5000/api/health

#### Step 8: Run Comprehensive Tests

```powershell
# Run the test script
python test_endpoints.py
```

This will test all API endpoints and create sample data.

**OR** Use the automated test suite:

```powershell
# Run pytest
pytest tests/ -v

# Run with coverage
pytest --cov=app tests/
```

**Expected Output:**
```
====== 10 passed in 0.82s ======
```

---

### Phase 3: GitHub Setup (20 minutes)

#### Step 9: Initialize Git Repository

```powershell
# Initialize git (if not already done)
git init

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Initial commit: Complete Kanban board application"
```

#### Step 10: Create GitHub Repository

1. **Go to GitHub:** https://github.com/new
2. **Repository Name:** `kanban`
3. **Description:** "Kanban board application - Coursera Agile Development Final Project"
4. **Visibility:** Public
5. **Do NOT** initialize with README (we already have one)
6. **Click:** "Create repository"

#### Step 11: Push to GitHub

```powershell
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/kanban.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Expected Output:**
```
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
...
To https://github.com/YOUR_USERNAME/kanban.git
 * [new branch]      main -> main
```

#### Step 12: Verify on GitHub

1. Go to your repository: `https://github.com/YOUR_USERNAME/kanban`
2. You should see all files uploaded
3. README.md should be displayed automatically

---

### Phase 4: Kanban Board Setup (15 minutes)

#### Step 13: Enable GitHub Projects

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Scroll to **"Features"** section
4. Check ✅ **"Projects"**
5. Click **"Save"**

#### Step 14: Create Kanban Board

1. Click **"Projects"** tab
2. Click **"New project"**
3. Select **"Board"** template
4. Name: **"Kanban Board"**
5. Click **"Create project"**

#### Step 15: Configure Columns

Rename/create columns:
- **Column 1:** "📝 New" (or "To Do")
- **Column 2:** "🔄 In Progress"
- **Column 3:** "✅ Done"

#### Step 16: Add User Stories

Copy user stories from `KANBAN_PLANNING.md` and add them as cards:

**Sprint 1 Stories (Add to "Done" column):**
- Set up GitHub repository
- Create documentation
- Define user stories
- Set up Kanban board
- Initialize project structure

**Sprint 2 Stories (Add to "In Progress" column):**
- Implement REST API endpoints
- Add task filtering
- Write unit tests
- Set up CI/CD pipeline

**Sprint 3 Stories (Add to "New" column):**
- Create Dockerfile
- Build Docker image
- Deploy application
- Configure monitoring

**Tip:** You can also create Issues and link them to the project board.

---

### Phase 5: Task 1 Screenshot (5 minutes)

#### Step 17: Prepare Screenshot

1. **Open two browser tabs:**
   - Tab 1: GitHub repository (showing files)
   - Tab 2: GitHub Projects board (showing Kanban board)

2. **Arrange windows side-by-side OR:**
   - Take two screenshots and merge them

3. **Ensure visible:**
   - Repository URL
   - README content preview
   - File structure (folders and files)
   - Kanban board with all columns
   - Multiple user stories visible

#### Step 18: Capture Screenshot

**Method 1: Windows Snip & Sketch**
```
Press: Win + Shift + S
Select: Rectangular snip
Capture the screen
Open Paint
Paste (Ctrl + V)
Save as: d:\Documents\GitHub\Coursera\kanban\screenshots\planning-repository-done.jpg
```

**Method 2: Browser Full Page Screenshot**
```
F12 (Open DevTools)
Ctrl + Shift + P
Type: screenshot
Select: Capture full size screenshot
Save to: screenshots\planning-repository-done.jpg
```

#### Step 19: Verify Screenshot

```powershell
# Check file exists
ls screenshots\planning-repository-done.jpg

# Verify file size (should be < 5MB)
(Get-Item screenshots\planning-repository-done.jpg).length/1MB
```

Open the file to ensure:
- [ ] High quality (readable text)
- [ ] Shows repository
- [ ] Shows Kanban board
- [ ] All required elements visible

---

### Phase 6: Task 2 - API Screenshots (20 minutes)

#### Step 20: Ensure Application is Running

```powershell
# In first terminal, make sure app is running
python run.py
```

#### Step 21: Test API and Capture Screenshots

Open browser to: http://localhost:5000/api/

**Required Screenshots:**

1. **api-url-running.jpg**
   - Browser showing http://localhost:5000/api/
   - API welcome message visible

2. **api-get-tasks.jpg**
   - Navigate to: http://localhost:5000/api/tasks
   - Shows all tasks in JSON format

3. **api-post-task.jpg**
   - Use Postman or curl to create a task
   - Capture the response

4. **api-get-task-by-id.jpg**
   - Navigate to: http://localhost:5000/api/tasks/1
   - Shows specific task details

5. **api-put-task.jpg**
   - Update a task using Postman/curl
   - Capture the response

6. **api-delete-task.jpg**
   - Delete a task using Postman/curl
   - Capture the response

**Tip:** Use `test_endpoints.py` to test all endpoints at once:

```powershell
python test_endpoints.py
```

Then screenshot the terminal output!

---

### Phase 7: Task 3 - CI/CD Pipeline (15 minutes)

#### Step 22: GitHub Actions Setup

**Good news!** The `.github/workflows/ci-build.yaml` file is already included.

When you push to GitHub, it will automatically run!

#### Step 23: Trigger Workflow

```powershell
# Make a small change to trigger workflow
echo "# Test" >> README.md

# Commit and push
git add README.md
git commit -m "Trigger GitHub Actions workflow"
git push
```

#### Step 24: View Workflow Run

1. Go to your GitHub repository
2. Click **"Actions"** tab
3. You should see a workflow running
4. Wait for it to complete (green checkmark)

#### Step 25: Capture Screenshots

1. **ci-workflow-run.jpg**
   - Actions tab showing successful run
   - Green checkmark visible

2. **github-actions-badge.jpg**
   - README with badge showing build status

3. **ci-build-yaml-file.jpg**
   - View `.github/workflows/ci-build.yaml` on GitHub
   - Show file contents

---

### Phase 8: Task 4 - Docker Deployment (20 minutes)

#### Step 26: Build Docker Image

```powershell
# Build the image
docker build -t kanban-app .

# This will take a few minutes...
```

**Expected Output:**
```
[+] Building 45.2s (10/10) FINISHED
=> [internal] load build definition from Dockerfile
...
=> => naming to docker.io/library/kanban-app
```

#### Step 27: Verify Docker Image

```powershell
# List Docker images
docker images
```

**Screenshot this!** Save as `docker-image.jpg`

#### Step 28: Run Docker Container

```powershell
# Stop the application in the first terminal (Ctrl+C)

# Run Docker container
docker run -d -p 5000:5000 --name kanban-app kanban-app

# Check container status
docker ps
```

**Screenshot this!** Save as `deployment-details.jpg`

#### Step 29: Test Dockerized Application

Open browser to: http://localhost:5000/api/

**Screenshot this!** Save as `application-page.jpg`

---

### Phase 9: Task 5 - Final Deliverables (10 minutes)

#### Step 30: Update Kanban Board

1. Move all completed stories to "Done" column
2. Ensure board reflects final state
3. Take screenshot: `final-kanban-board.jpg`

#### Step 31: Get Pipeline Logs

1. Go to GitHub Actions tab
2. Click on latest workflow run
3. Click on "build" job
4. View logs
5. Screenshot or download logs: `pipeline-logs.jpg`

---

## 🎉 Completion Checklist

Before submitting, verify you have:

### Code & Setup
- [ ] All files pushed to GitHub
- [ ] Repository is public
- [ ] README is complete
- [ ] Application runs locally
- [ ] All tests pass
- [ ] Docker image builds successfully

### Screenshots (20 total)
- [ ] planning-repository-done.jpg (Task 1)
- [ ] 6-8 screenshots for API testing (Task 2)
- [ ] 3-4 screenshots for CI/CD (Task 3)
- [ ] 4-5 screenshots for deployment (Task 4)
- [ ] 2 screenshots for final deliverables (Task 5)

### Documentation
- [ ] README.md is complete
- [ ] All documentation files present
- [ ] GitHub repository URL noted
- [ ] Screenshots are organized

---

## 🆘 Troubleshooting Common Issues

### Issue: "Module not found"
```powershell
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
```powershell
# Find and kill process
Get-Process -Id (Get-NetTCPConnection -LocalPort 5000).OwningProcess | Stop-Process -Force
```

### Issue: "Database locked"
```powershell
# Delete database and reinitialize
rm kanban.db
python init_db.py
```

### Issue: "Docker build failed"
```powershell
# Clear Docker cache
docker system prune -a
docker build --no-cache -t kanban-app .
```

### Issue: "Git push rejected"
```powershell
# Check remote
git remote -v

# Re-add remote
git remote set-url origin https://github.com/YOUR_USERNAME/kanban.git
git push -u origin main
```

---

## 📚 Next Steps

After completing all phases:

1. **Review all screenshots** - Ensure quality and completeness
2. **Test GitHub Actions** - Verify CI/CD pipeline runs successfully
3. **Document your work** - Add any additional notes
4. **Submit on Coursera** - Upload screenshots and repository URL
5. **Peer Review** - Evaluate other students' work

---

## ⏱️ Time Estimates

- **Phase 1-2:** Setup & Testing (25 min)
- **Phase 3:** GitHub Setup (20 min)
- **Phase 4:** Kanban Board (15 min)
- **Phase 5:** Task 1 Screenshot (5 min)
- **Phase 6:** Task 2 Screenshots (20 min)
- **Phase 7:** Task 3 CI/CD (15 min)
- **Phase 8:** Task 4 Docker (20 min)
- **Phase 9:** Task 5 Final (10 min)

**Total: ~2.5 hours**

---

## 🎓 Learning Outcomes

By completing this project, you have demonstrated:

- ✅ Agile sprint planning with Kanban
- ✅ RESTful API design and implementation
- ✅ Test-driven development with pytest
- ✅ Continuous Integration with GitHub Actions
- ✅ Containerization with Docker
- ✅ Git version control
- ✅ Technical documentation
- ✅ Software deployment

**Congratulations on completing the Agile Development and DevOps Final Project! 🚀**

---

## 📞 Additional Resources

- **Project Documentation:**
  - SUBMISSION_GUIDE.md - Complete submission guide
  - TASK1_INSTRUCTIONS.md - Detailed Task 1 steps
  - API_TESTING.md - API testing guide
  - DEPLOYMENT.md - Deployment instructions
  - QUICK_REFERENCE.md - Quick command reference

- **Support:**
  - Coursera Discussion Forums
  - Course materials and lectures
  - Office hours (if available)

---

**Good luck with your submission! 🎯**
