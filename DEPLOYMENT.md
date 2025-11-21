# Deployment Guide

This guide covers deploying the Kanban application using Docker and various hosting platforms.

## Table of Contents
1. [Local Docker Deployment](#local-docker-deployment)
2. [Docker Compose](#docker-compose)
3. [Cloud Deployment Options](#cloud-deployment-options)
4. [CI/CD Pipeline](#cicd-pipeline)

---

## Local Docker Deployment

### Build Docker Image

```bash
# Build the image
docker build -t kanban-app:latest .

# Verify the image was created
docker images | grep kanban-app
```

**Screenshot Required:** Output of `docker images` showing kanban-app

### Run Docker Container

```bash
# Run the container
docker run -d \
  --name kanban-app \
  -p 5000:5000 \
  kanban-app:latest

# Check container is running
docker ps
```

### Test the Deployment

```bash
# Health check
curl http://localhost:5000/api/health

# Get all tasks
curl http://localhost:5000/api/tasks
```

**Screenshot Required:** Browser showing application at http://localhost:5000/api/

### View Container Logs

```bash
# View logs
docker logs kanban-app

# Follow logs in real-time
docker logs -f kanban-app
```

### Stop and Remove Container

```bash
# Stop the container
docker stop kanban-app

# Remove the container
docker rm kanban-app

# Remove the image
docker rmi kanban-app:latest
```

---

## Docker Compose

Docker Compose simplifies multi-container deployments. Use this for production-like environments.

### Run with Docker Compose

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

**Screenshot Required:** Output of `docker-compose ps` showing running services

---

## Cloud Deployment Options

### Option 1: Heroku

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Deployment Steps

```bash
# Login to Heroku
heroku login

# Create new app
heroku create kanban-app-yourname

# Deploy using Docker
heroku container:push web
heroku container:release web

# Open the app
heroku open
```

**Application URL:** `https://kanban-app-yourname.herokuapp.com`

---

### Option 2: Railway

#### Prerequisites
- Railway account
- Railway CLI (optional)

#### Deployment Steps

1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub repository
5. Railway auto-detects Dockerfile and deploys

**Environment Variables:**
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

---

### Option 3: Render

#### Prerequisites
- Render account
- GitHub repository

#### Deployment Steps

1. Go to [render.com](https://render.com)
2. Click "New Web Service"
3. Connect GitHub repository
4. Configure:
   - **Build Command:** `docker build -t kanban-app .`
   - **Start Command:** `docker run -p 5000:5000 kanban-app`
   - **Environment:** Docker
   - **Port:** 5000

**Screenshot Required:** Render dashboard showing deployed service

---

### Option 4: Google Cloud Run

#### Prerequisites
- Google Cloud account
- gcloud CLI installed

#### Deployment Steps

```bash
# Authenticate
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/kanban-app

# Deploy to Cloud Run
gcloud run deploy kanban-app \
  --image gcr.io/YOUR_PROJECT_ID/kanban-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Get service URL
gcloud run services describe kanban-app --region us-central1
```

---

### Option 5: AWS ECS (Elastic Container Service)

#### Prerequisites
- AWS account
- AWS CLI configured
- ECR repository created

#### Deployment Steps

```bash
# Authenticate to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag kanban-app:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/kanban-app:latest

# Push to ECR
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/kanban-app:latest

# Deploy using ECS CLI or Console
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

The `.github/workflows/ci-build.yaml` file automates:
- Testing on multiple Python versions
- Code linting
- Docker image building
- Deployment (optional)

### View Pipeline Status

1. Go to your GitHub repository
2. Click on "Actions" tab
3. View workflow runs

**Screenshot Required:** 
- GitHub Actions tab showing successful run
- Badge in README showing build status

### Add GitHub Actions Badge

Add this to your README.md:

```markdown
![CI Build](https://github.com/YOUR_USERNAME/kanban/actions/workflows/ci-build.yaml/badge.svg)
```

---

## Production Checklist

Before deploying to production:

- [ ] Set `FLASK_ENV=production`
- [ ] Use strong SECRET_KEY
- [ ] Enable HTTPS
- [ ] Set up proper database (PostgreSQL instead of SQLite)
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Enable backups
- [ ] Configure rate limiting
- [ ] Add authentication if needed
- [ ] Review security headers

---

## Environment Variables

Create a `.env` file for production:

```bash
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:password@host:5432/kanban
ALLOWED_ORIGINS=https://yourdomain.com
```

**Note:** Never commit `.env` file to Git!

---

## Monitoring and Logs

### Docker Logs

```bash
# View logs
docker logs kanban-app

# Follow logs
docker logs -f kanban-app

# View last 100 lines
docker logs --tail 100 kanban-app
```

### Health Check Endpoint

The `/api/health` endpoint can be used for:
- Load balancer health checks
- Monitoring tools
- Uptime monitoring services

**Example with curl:**
```bash
curl http://localhost:5000/api/health
```

---

## Backup and Recovery

### Database Backup

```bash
# Copy database from container
docker cp kanban-app:/app/kanban.db ./backup/kanban-$(date +%Y%m%d).db

# Restore database
docker cp ./backup/kanban-20231121.db kanban-app:/app/kanban.db
docker restart kanban-app
```

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs kanban-app

# Check container details
docker inspect kanban-app

# Verify image
docker images
```

### Port Already in Use

```bash
# Find process using port 5000
# On Windows PowerShell:
Get-NetTCPConnection -LocalPort 5000

# Kill the process or use different port
docker run -p 8080:5000 kanban-app
```

### Database Issues

```bash
# Recreate database
docker exec kanban-app rm /app/kanban.db
docker restart kanban-app
```

---

## Screenshots Required for Task 4

- [ ] Screenshot of Docker image build output
- [ ] Screenshot of `docker images` showing kanban-app
- [ ] Screenshot of `docker ps` showing running container
- [ ] Screenshot of application running in browser
- [ ] Screenshot of deployment details (hosting platform dashboard)
- [ ] Screenshot of Sprint 3 Kanban board

---

## Next Steps

After successful deployment:
1. Test all API endpoints in production
2. Set up monitoring alerts
3. Configure automated backups
4. Document the production URL
5. Share with stakeholders
