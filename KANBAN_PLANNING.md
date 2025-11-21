# Kanban Board - User Stories and Sprint Planning

## Product Backlog

### User Stories

#### Epic: Basic Task Management
1. **As a** user, **I want to** create a new task **so that** I can track work items on the Kanban board.
   - **Acceptance Criteria:**
     - User can create a task with title, description, priority, and assigned person
     - Task is added to the "New" column by default
     - Task gets a unique ID
   - **Story Points:** 3
   - **Priority:** High

2. **As a** user, **I want to** view all tasks **so that** I can see the current state of work.
   - **Acceptance Criteria:**
     - User can view all tasks in the Kanban board
     - Tasks are organized by status columns (New, In Progress, Done)
     - Each task displays key information
   - **Story Points:** 2
   - **Priority:** High

3. **As a** user, **I want to** update task status **so that** I can move tasks through the workflow.
   - **Acceptance Criteria:**
     - User can change task status (New → In Progress → Done)
     - Task updates are reflected immediately
     - Timestamp is updated on changes
   - **Story Points:** 3
   - **Priority:** High

4. **As a** user, **I want to** delete a task **so that** I can remove completed or obsolete items.
   - **Acceptance Criteria:**
     - User can delete any task
     - Confirmation is required before deletion
     - Task is permanently removed from the system
   - **Story Points:** 2
   - **Priority:** Medium

#### Epic: REST API
5. **As a** developer, **I want to** have REST API endpoints **so that** I can integrate with other systems.
   - **Acceptance Criteria:**
     - GET /api/tasks returns all tasks
     - POST /api/tasks creates a new task
     - PUT /api/tasks/<id> updates a task
     - DELETE /api/tasks/<id> deletes a task
     - All endpoints return proper HTTP status codes
   - **Story Points:** 5
   - **Priority:** High

6. **As a** developer, **I want to** filter tasks by status **so that** I can retrieve specific subsets of tasks.
   - **Acceptance Criteria:**
     - GET /api/tasks?status=New returns only new tasks
     - Filter works for all status values
     - Returns empty array if no tasks match
   - **Story Points:** 2
   - **Priority:** Medium

#### Epic: CI/CD Pipeline
7. **As a** developer, **I want to** have automated tests **so that** I can ensure code quality.
   - **Acceptance Criteria:**
     - Unit tests cover all API endpoints
     - Tests run automatically on push
     - Test coverage is > 80%
   - **Story Points:** 5
   - **Priority:** High

8. **As a** developer, **I want to** have CI/CD pipeline **so that** code is automatically tested and built.
   - **Acceptance Criteria:**
     - GitHub Actions workflow runs on push/PR
     - Tests run on multiple Python versions
     - Docker image is built and tested
   - **Story Points:** 5
   - **Priority:** High

#### Epic: Deployment
9. **As a** developer, **I want to** containerize the application **so that** it can run consistently anywhere.
   - **Acceptance Criteria:**
     - Dockerfile builds successfully
     - Container runs the application
     - Application is accessible on port 5000
   - **Story Points:** 3
   - **Priority:** High

10. **As a** user, **I want to** have the application deployed **so that** I can access it online.
    - **Acceptance Criteria:**
      - Application is deployed to a hosting service
      - Application is accessible via URL
      - Health check endpoint confirms it's running
    - **Story Points:** 3
    - **Priority:** Medium

---

## Sprint Planning

### Sprint 1: Setup and Foundation (Week 1)
**Goal:** Set up repository, define user stories, and create project structure

**Selected Stories:**
- Set up GitHub repository ✓
- Create README and documentation ✓
- Define all user stories ✓
- Set up project structure ✓
- Create initial Kanban board ✓

**Sprint Review:**
- Repository created with proper structure
- All documentation in place
- Kanban board configured with columns: New, In Progress, Done
- User stories defined and prioritized

---

### Sprint 2: REST API Development (Week 2)
**Goal:** Implement REST API and automated testing

**Selected Stories:**
- Story #5: REST API endpoints (5 pts)
- Story #6: Filter tasks by status (2 pts)
- Story #7: Automated tests (5 pts)
- Story #8: CI/CD pipeline (5 pts)

**Total Story Points:** 17

**Tasks:**
1. Create Flask application structure
2. Implement Task model with SQLAlchemy
3. Implement GET /api/tasks endpoint
4. Implement POST /api/tasks endpoint
5. Implement PUT /api/tasks/<id> endpoint
6. Implement DELETE /api/tasks/<id> endpoint
7. Add status filtering functionality
8. Write unit tests for all endpoints
9. Set up GitHub Actions workflow
10. Configure pytest and coverage reporting

**Definition of Done:**
- All API endpoints implemented and working
- Unit tests passing with >80% coverage
- CI/CD pipeline running successfully
- GitHub Actions badge showing build status

---

### Sprint 3: Deployment and Containerization (Week 3)
**Goal:** Containerize application and deploy to production

**Selected Stories:**
- Story #1: Create tasks (3 pts)
- Story #2: View tasks (2 pts)
- Story #3: Update task status (3 pts)
- Story #4: Delete tasks (2 pts)
- Story #9: Containerize application (3 pts)
- Story #10: Deploy application (3 pts)

**Total Story Points:** 16

**Tasks:**
1. Create Dockerfile for the application
2. Build Docker image
3. Test Docker container locally
4. Implement task creation functionality
5. Implement task viewing functionality
6. Implement task update functionality
7. Implement task deletion functionality
8. Set up deployment environment
9. Deploy application to hosting service
10. Verify deployment and run smoke tests

**Definition of Done:**
- Docker image builds successfully
- Application runs in container
- All CRUD operations working
- Application deployed and accessible
- Health check endpoint responding

---

## Kanban Board Columns

### New (To Do)
- User stories that are ready to be worked on
- Prioritized from top to bottom

### In Progress
- Stories currently being developed
- Limit: 3 items (WIP limit)

### Testing
- Stories completed and ready for testing
- Automated tests must pass

### Done
- Stories that meet Definition of Done
- Reviewed and approved

---

## Story Points Reference

- **1 point:** Very small, < 2 hours
- **2 points:** Small, 2-4 hours
- **3 points:** Medium, 4-8 hours (1 day)
- **5 points:** Large, 8-16 hours (2 days)
- **8 points:** Very large, needs to be broken down

---

## Definition of Done

A user story is considered "Done" when:
1. Code is written and meets requirements
2. Unit tests are written and passing
3. Code is reviewed
4. Code is merged to main branch
5. CI/CD pipeline passes
6. Documentation is updated
7. Acceptance criteria are met

---

## Team Information

**Team Name:** Kanban Development Team
**Sprint Duration:** 1 week
**Team Velocity:** ~15-20 story points per sprint

**Team Members:**
- Product Owner: [Your Name]
- Scrum Master: [Your Name]
- Developer: [Your Name]
- Tester: [Your Name]

---

## Notes

- This Kanban board follows Agile/Scrum principles
- Daily standups track progress
- Sprint retrospectives identify improvements
- Continuous integration ensures code quality
