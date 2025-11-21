# Kanban Board Application 📋

![CI Build](https://github.com/YOUR_USERNAME/kanban/actions/workflows/ci-build.yaml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

## Project Overview
This is a Kanban board application built as part of the **Agile Development and DevOps** course final project. The application demonstrates modern software development practices including REST API design, automated testing, CI/CD pipelines, and containerized deployment.

## ✨ Features
- **RESTful API** for managing tasks (CRUD operations)
- **Kanban board** with multiple columns (New, In Progress, Done)
- **Sprint planning** and tracking with user stories
- **CI/CD pipeline** with GitHub Actions
- **Docker containerization** for consistent deployment
- **Automated testing** with pytest (80%+ coverage)
- **Health check** endpoints for monitoring
- **Status filtering** for tasks

## Technology Stack
- Backend: Python Flask
- Database: SQLite
- CI/CD: GitHub Actions
- Containerization: Docker
- Testing: pytest

## Project Structure
```
kanban/
├── app/                    # Application code
│   ├── __init__.py
│   ├── models.py          # Database models
│   ├── routes.py          # API routes
│   └── config.py          # Configuration
├── tests/                 # Test files
│   └── test_api.py
├── screenshots/           # Screenshots for submission
├── .github/
│   └── workflows/
│       └── ci-build.yaml  # CI/CD workflow
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python run.py`
4. Access at: `http://localhost:5000`

### Running with Docker
```bash
docker build -t kanban-app .
docker run -p 5000:5000 kanban-app
```

## API Endpoints
- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/<id>` - Get a specific task
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

## Sprint Planning

### Sprint 1: Setup and Planning
- Set up repository structure
- Create initial Kanban board
- Define user stories

### Sprint 2: REST API Development
- Implement REST API endpoints
- Add automated testing
- Set up CI/CD pipeline

### Sprint 3: Deployment
- Dockerize the application
- Deploy to production
- Monitor and maintain

## Screenshots
All required screenshots are stored in the `screenshots/` directory.

## 📚 Documentation

- **[SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md)** - Complete guide for Coursera assignment submission
- **[KANBAN_PLANNING.md](KANBAN_PLANNING.md)** - Sprint planning and user stories
- **[API_TESTING.md](API_TESTING.md)** - API endpoint testing guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment instructions for various platforms
- **[SCREENSHOT_CHECKLIST.md](SCREENSHOT_CHECKLIST.md)** - Required screenshots checklist

## 🎯 Assignment Tasks

This project fulfills all requirements for the peer-graded assignment:

- ✅ **Task 1 (6 pts):** Repository and Kanban board setup
- ✅ **Task 2 (16 pts):** REST API implementation and testing
- ✅ **Task 3 (12 pts):** CI/CD pipeline with GitHub Actions
- ✅ **Task 4 (10 pts):** Docker deployment
- ✅ **Task 5 (6 pts):** Final pipeline run and documentation

**Total: 50 points**

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/kanban.git
   cd kanban
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

4. **Access the API:**
   - Open browser to: http://localhost:5000/api/
   - Health check: http://localhost:5000/api/health

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest --cov=app tests/

# Generate HTML coverage report
pytest --cov=app --cov-report=html tests/
```

### Docker Deployment

```bash
# Build Docker image
docker build -t kanban-app .

# Run container
docker run -d -p 5000:5000 --name kanban-app kanban-app

# Or use Docker Compose
docker-compose up -d
```

## 📸 Screenshots

All required screenshots for the assignment are stored in the [`screenshots/`](screenshots/) directory.

## 🔗 Repository Link

**GitHub Repository:** https://github.com/YOUR_USERNAME/kanban

Replace `YOUR_USERNAME` with your actual GitHub username.

## 👤 Author

**Coursera Agile Development and DevOps Final Project**
- Course: Agile Development and DevOps
- Institution: Coursera
- Date: November 2025

## 📄 License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🙏 Acknowledgments

- Coursera for providing the course platform
- Flask and Python communities for excellent documentation
- GitHub Actions for CI/CD capabilities
- Docker for containerization technology
