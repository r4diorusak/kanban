# Task 1: Creating planning-repository-done.jpg

## Overview
Task 1a requires you to upload a screenshot named `planning-repository-done.jpg` that demonstrates your repository setup and Kanban board planning phase.

## What This Screenshot Should Show

### Required Elements:
1. ✅ **GitHub Repository**
   - Repository name: "kanban"
   - README.md file visible
   - File structure visible (folders: app/, tests/, .github/, etc.)
   - At least 10+ files committed

2. ✅ **Kanban Board**
   - Board name clearly visible
   - Three columns: "New" (or "To Do"), "In Progress", "Done"
   - Multiple user stories/cards visible
   - Cards should have titles and descriptions

3. ✅ **Sprint Planning Evidence**
   - User stories organized by sprints
   - Sprint 1, Sprint 2, Sprint 3 labels
   - Priority tags (High, Medium, Low)
   - Story points visible (optional but recommended)

### Recommended Layout:
- Split screen showing repository AND Kanban board
- OR two separate sections in one screenshot
- OR composite image with both views

---

## Step-by-Step Instructions

### Step 1: Set Up GitHub Repository

1. **Create Repository:**
   ```bash
   # Navigate to project directory
   cd d:\Documents\GitHub\Coursera\kanban
   
   # Initialize Git (if not already done)
   git init
   
   # Add all files
   git add .
   
   # Commit
   git commit -m "Initial commit: Kanban board application with REST API, CI/CD, and Docker support"
   ```

2. **Create GitHub Repository:**
   - Go to https://github.com/new
   - Repository name: `kanban`
   - Description: "Kanban board application - Coursera Agile Development and DevOps Final Project"
   - Public repository
   - Do NOT initialize with README (we already have one)
   - Click "Create repository"

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/kanban.git
   git branch -M main
   git push -u origin main
   ```

4. **Verify Upload:**
   - Refresh GitHub repository page
   - Ensure all files are visible
   - README.md should be displayed automatically

---

### Step 2: Create Kanban Board

#### Option A: GitHub Projects (Recommended)

1. **Enable Projects:**
   - Go to your repository on GitHub
   - Click "Settings" tab
   - Scroll to "Features" section
   - Enable "Projects"

2. **Create New Project:**
   - Click "Projects" tab
   - Click "New project"
   - Click "Board" (classic Kanban view)
   - Name: "Kanban Board - Sprint Planning"
   - Click "Create"

3. **Set Up Columns:**
   - Rename existing columns or create new ones:
     - Column 1: "📝 New" (or "To Do")
     - Column 2: "🔄 In Progress"
     - Column 3: "✅ Done"

4. **Add User Stories:**
   
   Copy these user stories from `KANBAN_PLANNING.md`:
   
   **Sprint 1 - Setup (New Column):**
   - "Set up GitHub repository and project structure"
   - "Create README and documentation"
   - "Define user stories and acceptance criteria"
   - "Set up Kanban board with columns"
   - "Initialize Python project with dependencies"
   
   **Sprint 2 - Development (New Column):**
   - "Implement REST API endpoints (GET, POST, PUT, DELETE)"
   - "Add status filtering for tasks"
   - "Write unit tests for all API endpoints"
   - "Set up CI/CD pipeline with GitHub Actions"
   - "Configure automated testing and linting"
   
   **Sprint 3 - Deployment (New Column):**
   - "Create Dockerfile for containerization"
   - "Build and test Docker image"
   - "Deploy application to hosting platform"
   - "Set up health monitoring endpoints"
   - "Document deployment process"

5. **Add Labels/Tags:**
   - Sprint 1 (green label)
   - Sprint 2 (blue label)
   - Sprint 3 (purple label)
   - High Priority (red)
   - Medium Priority (yellow)
   - Low Priority (gray)

6. **Assign Story Points:**
   - Add story points to each card (1, 2, 3, 5, 8)
   - Document in card description

---

#### Option B: GitHub Issues + Projects

1. **Create Issues for User Stories:**
   - Go to "Issues" tab
   - Click "New issue"
   - Title: User story title
   - Description: Acceptance criteria
   - Labels: Sprint, Priority
   - Create issue

2. **Link to Project:**
   - Create project board
   - Add issues to board
   - Organize by column

---

### Step 3: Prepare for Screenshot

1. **Verify Repository View:**
   - Navigate to repository main page
   - Ensure README is visible
   - File tree should show:
     ```
     kanban/
     ├── .github/
     │   └── workflows/
     │       └── ci-build.yaml
     ├── app/
     │   ├── __init__.py
     │   ├── models.py
     │   └── routes.py
     ├── tests/
     │   └── test_api.py
     ├── screenshots/
     ├── Dockerfile
     ├── docker-compose.yml
     ├── requirements.txt
     ├── run.py
     └── README.md
     ```

2. **Verify Kanban Board:**
   - Open Projects tab
   - View your Kanban board
   - Ensure columns are named correctly
   - Check that cards are visible with titles

3. **Arrange Windows:**
   - **Option 1:** Split screen (Repository left, Board right)
   - **Option 2:** Full screen repository, then board (take 2 screenshots, merge later)
   - **Option 3:** Use browser tab capture extension

---

### Step 4: Capture Screenshot

#### Method 1: Windows Snipping Tool (Recommended)

1. Press `Win + Shift + S`
2. Select rectangular snip
3. Capture the screen showing:
   - GitHub repository page (left/top)
   - Kanban board (right/bottom)
4. Screenshot auto-copies to clipboard
5. Open Paint or image editor
6. Paste (Ctrl + V)
7. Save as: `planning-repository-done.jpg`

#### Method 2: Full Page Screenshot

1. Open browser DevTools (F12)
2. Press `Ctrl + Shift + P`
3. Type "screenshot"
4. Select "Capture full size screenshot"
5. Saves to Downloads folder
6. Rename to `planning-repository-done.jpg`

#### Method 3: Screenshot Extension

1. Install "Awesome Screenshot" browser extension
2. Click extension icon
3. Select "Capture entire page"
4. Edit/annotate if needed
5. Save as `planning-repository-done.jpg`

#### Method 4: Composite Image

1. Take screenshot of repository
2. Take screenshot of Kanban board
3. Use image editor (Paint, GIMP, Photoshop)
4. Create new canvas (1920x1080 or larger)
5. Paste repository screenshot (top)
6. Paste board screenshot (bottom)
7. Add divider line
8. Save as `planning-repository-done.jpg`

---

### Step 5: Verify Screenshot Quality

#### Checklist:
- [ ] Resolution: At least 1280x720 pixels
- [ ] Format: JPG (JPEG)
- [ ] File size: Less than 5MB
- [ ] All text is readable
- [ ] Repository name visible
- [ ] README.md visible
- [ ] File structure visible
- [ ] Kanban board visible
- [ ] Column names visible ("New", "In Progress", "Done")
- [ ] At least 5 user stories visible
- [ ] Colors and labels visible
- [ ] No personal/sensitive information shown
- [ ] GitHub URL visible in address bar

---

### Step 6: Save Screenshot

1. **Save Location:**
   ```
   d:\Documents\GitHub\Coursera\kanban\screenshots\planning-repository-done.jpg
   ```

2. **Verify File:**
   - Open the image to ensure quality
   - Check file size
   - Ensure correct filename

3. **Optional - Add to Repository:**
   ```bash
   git add screenshots/planning-repository-done.jpg
   git commit -m "Add Task 1 screenshot: planning-repository-done.jpg"
   git push
   ```

---

## Example Screenshot Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ GitHub Repository - kanban                                      │
│ https://github.com/YOUR_USERNAME/kanban                         │
├─────────────────────────────────────────────────────────────────┤
│ README.md                                                        │
│ # Kanban Board Application 📋                                   │
│                                                                  │
│ 📁 .github/workflows     📁 app/        📁 tests/              │
│ 📄 Dockerfile            📄 README.md   📄 requirements.txt    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Kanban Board - Sprint Planning                                  │
│                                                                  │
│ ┌─────────┬─────────────────┬──────────┐                       │
│ │   New   │  In Progress    │   Done   │                       │
│ ├─────────┼─────────────────┼──────────┤                       │
│ │ Story 1 │                 │          │                       │
│ │ Story 2 │                 │          │                       │
│ │ Story 3 │                 │          │                       │
│ │ Story 4 │                 │          │                       │
│ │ Story 5 │                 │          │                       │
│ └─────────┴─────────────────┴──────────┘                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Common Issues and Solutions

### Issue 1: Can't See Kanban Board
**Solution:** 
- Ensure GitHub Projects is enabled in repository settings
- Make project public
- Refresh page

### Issue 2: Screenshot Too Large
**Solution:**
- Compress image using online tools (TinyJPG, Compressor.io)
- Or resize in image editor
- Target: Under 5MB

### Issue 3: Screenshot Too Small/Blurry
**Solution:**
- Use higher resolution
- Take screenshot in full screen mode
- Use proper screen capture tool
- Don't zoom out too much in browser

### Issue 4: Repository Empty
**Solution:**
```bash
# Verify files exist
ls

# Check git status
git status

# Re-add files if needed
git add .
git commit -m "Add all project files"
git push origin main
```

### Issue 5: Kanban Board Empty
**Solution:**
- Add user stories manually
- Or import from Issues
- Ensure cards are not hidden

---

## Grading Criteria for Task 1

Peer reviewers will check:

1. **Repository Setup (3 points):**
   - [ ] Repository exists and is accessible
   - [ ] README.md is present and informative
   - [ ] Proper file structure with multiple directories
   - [ ] At least 10+ files committed

2. **Kanban Board Setup (3 points):**
   - [ ] Board has proper columns (New, In Progress, Done)
   - [ ] Multiple user stories are visible (at least 5)
   - [ ] Stories are organized and labeled
   - [ ] Sprint planning is evident

**Total: 6 points**

---

## Alternative: If Using ZenHub

If using ZenHub instead of GitHub Projects:

1. Install ZenHub browser extension
2. Go to repository
3. Click "Boards" tab
4. Create pipelines: New, In Progress, Review, Done
5. Add issues to pipelines
6. Take screenshot showing ZenHub board
7. Save as `planning-repository-done.jpg`

**Note:** The assignment accepts both GitHub Projects and ZenHub screenshots.

---

## Final Checklist

Before submitting Task 1:

- [ ] GitHub repository created and public
- [ ] All code pushed to repository
- [ ] README.md visible on repository page
- [ ] Kanban board created with 3+ columns
- [ ] 10+ user stories added to board
- [ ] Stories organized by Sprint
- [ ] Labels/priorities assigned
- [ ] Screenshot captured showing both repository and board
- [ ] Screenshot saved as `planning-repository-done.jpg`
- [ ] Screenshot quality verified (readable, high-res)
- [ ] File size under 5MB
- [ ] Screenshot uploaded to Coursera assignment

---

## Next Steps

After completing Task 1:
1. Move to Task 2: REST API implementation
2. Follow instructions in `API_TESTING.md`
3. Continue with remaining tasks
4. Refer to `SUBMISSION_GUIDE.md` for complete workflow

---

**Good luck with your submission! 🎉**
