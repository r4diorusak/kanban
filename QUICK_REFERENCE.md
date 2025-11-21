# Kanban Board Application - Quick Reference

## Project Structure
```
kanban/
├── .github/workflows/      # CI/CD configurations
│   └── ci-build.yaml      # GitHub Actions workflow
├── app/                   # Application code
│   ├── __init__.py       # Flask app initialization
│   ├── models.py         # Database models
│   └── routes.py         # API routes/endpoints
├── tests/                # Automated tests
│   └── test_api.py      # API endpoint tests
├── screenshots/          # Assignment screenshots
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Quick Commands

### Setup & Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python run.py

# Run tests
pytest tests/ -v

# Run with coverage
pytest --cov=app tests/
```

### Docker
```bash
# Build image
docker build -t kanban-app .

# Run container
docker run -p 5000:5000 kanban-app

# Docker Compose
docker-compose up -d
```

### Git
```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/kanban.git
git push -u origin main

# Update
git add .
git commit -m "Update message"
git push
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/` | API information |
| GET | `/api/health` | Health check |
| GET | `/api/tasks` | Get all tasks |
| GET | `/api/tasks/<id>` | Get specific task |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/<id>` | Update task |
| DELETE | `/api/tasks/<id>` | Delete task |

## Test API with curl

```bash
# Health check
curl http://localhost:5000/api/health

# Get all tasks
curl http://localhost:5000/api/tasks

# Create task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Task","description":"Testing","status":"New"}'

# Update task
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"In Progress"}'

# Delete task
curl -X DELETE http://localhost:5000/api/tasks/1
```

## Assignment Tasks Summary

1. **Task 1 (6 pts):** Repository + Kanban board setup
   - Screenshot: `planning-repository-done.jpg`

2. **Task 2 (16 pts):** REST API implementation
   - Screenshots: API responses for all endpoints

3. **Task 3 (12 pts):** CI/CD pipeline
   - Screenshots: GitHub Actions workflow + badge

4. **Task 4 (10 pts):** Docker deployment
   - Screenshots: Docker image + running app

5. **Task 5 (6 pts):** Final deliverables
   - Screenshots: Final board + pipeline logs

## User Stories (from KANBAN_PLANNING.md)

### Sprint 1 - Setup
- Set up GitHub repository ✓
- Create documentation ✓
- Define user stories ✓
- Initialize project structure ✓

### Sprint 2 - Development
- Implement REST API endpoints
- Add filtering functionality
- Write unit tests
- Set up CI/CD pipeline

### Sprint 3 - Deployment
- Create Dockerfile
- Build Docker image
- Deploy application
- Document deployment

## Documentation Files

- **SUBMISSION_GUIDE.md** - Complete assignment guide
- **TASK1_INSTRUCTIONS.md** - Detailed Task 1 steps
- **KANBAN_PLANNING.md** - Sprint planning & user stories
- **API_TESTING.md** - API testing guide
- **DEPLOYMENT.md** - Deployment instructions
- **SCREENSHOT_CHECKLIST.md** - Screenshot requirements

## Status Columns

- **New:** Tasks ready to be started
- **In Progress:** Currently being worked on
- **Done:** Completed tasks

## Story Points Guide

- **1 point:** < 2 hours
- **2 points:** 2-4 hours
- **3 points:** 4-8 hours (1 day)
- **5 points:** 8-16 hours (2 days)
- **8 points:** Needs breakdown

## Priorities

- 🔴 **High:** Critical, must complete
- 🟡 **Medium:** Important, should complete
- ⚪ **Low:** Nice to have

## GitHub Setup Steps

1. Create repository on GitHub
2. Enable GitHub Projects
3. Create Kanban board
4. Add user stories as issues/cards
5. Organize by Sprint labels
6. Take screenshot for Task 1

## Troubleshooting

### Port in use
```bash
# Windows PowerShell
Get-Process -Id (Get-NetTCPConnection -LocalPort 5000).OwningProcess | Stop-Process -Force
```

### Module not found
```bash
pip install -r requirements.txt
```

### Database error
```bash
# Delete and recreate
rm kanban.db
python run.py
```

## Important URLs

- **Local:** http://localhost:5000/api/
- **GitHub:** https://github.com/YOUR_USERNAME/kanban
- **GitHub Actions:** https://github.com/YOUR_USERNAME/kanban/actions

## Assignment Deadline

**Due:** November 25, 11:59 PM WIB

## File Naming Convention

Screenshots should be saved as:
- `planning-repository-done.jpg` (Task 1)
- `sprint2-*.jpg` (Task 2)
- `ci-*.jpg` (Task 3)
- `docker-*.jpg` (Task 4)
- `final-*.jpg` (Task 5)

## Badge for README

```markdown
![CI Build](https://github.com/YOUR_USERNAME/kanban/actions/workflows/ci-build.yaml/badge.svg)
```

Replace `YOUR_USERNAME` with your GitHub username.

---

**For detailed instructions, refer to the respective documentation files.**
