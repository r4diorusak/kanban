# Sprint 2 Planning - REST API & CI/CD Implementation

## Sprint 2 Overview
**Duration:** Week 2  
**Focus:** REST API Implementation and CI/CD Pipeline Setup  
**Team:** Full Stack Development Team  

---

## Sprint 2 Goals
1. ✅ Implement complete REST API with CRUD operations
2. ✅ Add status filtering functionality
3. 🔄 Create comprehensive unit tests
4. 🔄 Setup CI/CD pipeline with GitHub Actions

---

## User Stories for Sprint 2

### 🔄 In Progress

#### User Story #6: Implement REST API endpoints (GET, POST, PUT, DELETE)
**Status:** In Progress  
**Priority:** High  
**Story Points:** 5  
**Assigned To:** Backend Developer

**Description:**
Create RESTful API endpoints for complete task management:
- GET /api/tasks - List all tasks
- GET /api/tasks/<id> - Get single task
- POST /api/tasks - Create new task
- PUT /api/tasks/<id> - Update task
- DELETE /api/tasks/<id> - Delete task

**Acceptance Criteria:**
- [x] GET endpoint returns all tasks with proper JSON format
- [x] POST endpoint creates new task and returns 201 status
- [x] PUT endpoint updates existing task
- [x] DELETE endpoint removes task successfully
- [x] All endpoints handle errors properly
- [x] API returns appropriate HTTP status codes
- [x] Response format is consistent across all endpoints

**Progress:** 90% Complete - All endpoints implemented and tested

---

#### User Story #7: Add status filtering for tasks
**Status:** In Progress  
**Priority:** Medium  
**Story Points:** 2  
**Assigned To:** Backend Developer

**Description:**
Implement query parameter filtering to get tasks by status (New, In Progress, Done)

**Acceptance Criteria:**
- [x] GET /api/tasks?status=New returns only New tasks
- [x] GET /api/tasks?status=In Progress returns In Progress tasks
- [x] GET /api/tasks?status=Done returns completed tasks
- [ ] Invalid status returns appropriate error message
- [x] Filter is case-insensitive

**Progress:** 80% Complete - Basic filtering implemented

---

#### User Story #8: Write unit tests for all API endpoints
**Status:** In Progress  
**Priority:** High  
**Story Points:** 3  
**Assigned To:** QA Engineer / Backend Developer

**Description:**
Create comprehensive test suite using pytest to ensure API reliability

**Acceptance Criteria:**
- [ ] Test coverage >= 80%
- [ ] Tests for all CRUD operations
- [ ] Tests for error scenarios (404, 400, 500)
- [ ] Tests for status filtering
- [ ] Tests run successfully with pytest
- [ ] Mock database for testing

**Progress:** 40% Complete - Test structure created

---

#### User Story #9: Set up CI/CD pipeline with GitHub Actions
**Status:** In Progress  
**Priority:** High  
**Story Points:** 4  
**Assigned To:** DevOps Engineer

**Description:**
Configure automated testing and deployment using GitHub Actions

**Acceptance Criteria:**
- [ ] Create .github/workflows/ci-build.yaml
- [ ] Workflow runs on push and pull request
- [ ] Automated testing with pytest
- [ ] Code coverage reporting
- [ ] Build status badge in README
- [ ] Workflow notifications on failure

**Progress:** 30% Complete - Planning phase

---

## Sprint 2 Backlog (Todo)

### 📋 Todo

#### User Story #10: Create Dockerfile for containerization
**Status:** Todo  
**Priority:** Medium  
**Story Points:** 3  
**Sprint:** Sprint 3 (Planned)

#### User Story #11: Build and test Docker image
**Status:** Todo  
**Priority:** Medium  
**Story Points:** 2  
**Sprint:** Sprint 3 (Planned)

#### User Story #12: Deploy application to hosting platform
**Status:** Todo  
**Priority:** High  
**Story Points:** 4  
**Sprint:** Sprint 3 (Planned)

#### User Story #13: Set up health monitoring endpoints
**Status:** Todo  
**Priority:** Low  
**Story Points:** 2  
**Sprint:** Sprint 3 (Planned)

---

## Sprint 2 Progress Summary

| Status | Count | Story Points | Percentage |
|--------|-------|--------------|------------|
| ✅ Done (Sprint 1) | 5 | 15 | 38% |
| 🔄 In Progress (Sprint 2) | 4 | 14 | 31% |
| 📋 Todo (Sprint 3) | 4 | 11 | 31% |
| **Total** | **13** | **40** | **100%** |

---

## Sprint 2 Velocity
- **Planned Story Points:** 14
- **Completed Story Points:** 10 (estimated)
- **Remaining:** 4 points
- **Team Capacity:** 100%

---

## Key Achievements in Sprint 2
1. ✅ Complete REST API implementation with all CRUD operations
2. ✅ Status filtering functionality working
3. ✅ Successful API testing with Postman/Thunder Client
4. ✅ Database integration with SQLAlchemy
5. 🔄 Unit test framework setup in progress
6. 🔄 CI/CD pipeline planning in progress

---

## Blockers & Risks
- ⚠️ Unit test coverage needs improvement
- ⚠️ CI/CD workflow configuration pending
- ⚠️ Need to add error handling edge cases

---

## Next Sprint (Sprint 3) Preview
- Docker containerization
- Production deployment
- Monitoring & logging setup
- Performance optimization

---

**Sprint Review Date:** Week 2 End  
**Sprint Retrospective:** To be scheduled  
**Next Sprint Start:** Week 3

---

## Team Notes
- REST API endpoints fully functional
- Ready for CI/CD integration
- Documentation updated
- Moving toward deployment phase
