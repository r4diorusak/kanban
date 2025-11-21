# User Story Template

## Format Standar User Story

```
As a [type of user],
I want to [perform some action],
So that [achieve some goal/benefit].
```

---

## Example User Stories with Template

### User Story #1: Create Task

**User Story:**
```
As a user,
I want to create a new task,
So that I can track work items on the Kanban board.
```

**Acceptance Criteria:**
- [ ] User can enter task title (required field)
- [ ] User can enter task description (optional)
- [ ] User can set priority (High, Medium, Low)
- [ ] User can assign task to team member
- [ ] Task is automatically added to "New" column
- [ ] Task receives unique ID upon creation
- [ ] System displays success message
- [ ] Created task appears immediately on board

**Story Points:** 3

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** Backend Developer

---

### User Story #2: View All Tasks

**User Story:**
```
As a user,
I want to view all tasks on the Kanban board,
So that I can see the current state of work.
```

**Acceptance Criteria:**
- [ ] User can see all tasks organized by status columns
- [ ] Each task displays: title, priority, assignee
- [ ] Tasks are sorted by creation date (newest first)
- [ ] Empty columns show "No tasks" message
- [ ] Page loads within 2 seconds
- [ ] Tasks are color-coded by priority

**Story Points:** 2

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** Frontend Developer

---

### User Story #3: Update Task Status

**User Story:**
```
As a user,
I want to update the status of a task,
So that I can move tasks through the workflow.
```

**Acceptance Criteria:**
- [ ] User can change status from New → In Progress
- [ ] User can change status from In Progress → Done
- [ ] Status change is reflected immediately
- [ ] Timestamp is updated automatically
- [ ] System prevents invalid status transitions
- [ ] Confirmation message is displayed
- [ ] Task history is maintained

**Story Points:** 3

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** Backend Developer

---

### User Story #4: Delete Task

**User Story:**
```
As a user,
I want to delete a task,
So that I can remove completed or obsolete items.
```

**Acceptance Criteria:**
- [ ] User can click delete button on any task
- [ ] Confirmation dialog appears before deletion
- [ ] Task is removed from database permanently
- [ ] Board updates immediately after deletion
- [ ] Deleted task cannot be recovered
- [ ] System shows success notification

**Story Points:** 2

**Priority:** Medium

**Sprint:** Sprint 2

**Assigned To:** Backend Developer

---

### User Story #5: REST API Implementation

**User Story:**
```
As a developer,
I want to have REST API endpoints,
So that I can integrate with other systems.
```

**Acceptance Criteria:**
- [ ] GET /api/tasks returns all tasks
- [ ] POST /api/tasks creates new task
- [ ] GET /api/tasks/<id> returns specific task
- [ ] PUT /api/tasks/<id> updates task
- [ ] DELETE /api/tasks/<id> deletes task
- [ ] All endpoints return proper HTTP status codes
- [ ] Responses are in JSON format
- [ ] API includes error handling
- [ ] API documentation is available

**Story Points:** 5

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** Backend Team

---

### User Story #6: Filter Tasks by Status

**User Story:**
```
As a developer,
I want to filter tasks by status,
So that I can retrieve specific subsets of tasks via API.
```

**Acceptance Criteria:**
- [ ] GET /api/tasks?status=New returns only new tasks
- [ ] GET /api/tasks?status=In Progress returns tasks in progress
- [ ] GET /api/tasks?status=Done returns completed tasks
- [ ] Invalid status returns empty array
- [ ] Filter is case-insensitive
- [ ] Response includes count of filtered tasks

**Story Points:** 2

**Priority:** Medium

**Sprint:** Sprint 2

**Assigned To:** Backend Developer

---

### User Story #7: Automated Testing

**User Story:**
```
As a developer,
I want to have automated tests,
So that I can ensure code quality and catch bugs early.
```

**Acceptance Criteria:**
- [ ] Unit tests cover all API endpoints
- [ ] Test coverage is > 80%
- [ ] Tests run automatically on git push
- [ ] Failed tests prevent merge
- [ ] Test results are displayed in CI/CD
- [ ] Tests include positive and negative cases
- [ ] Tests verify response structure
- [ ] Tests check error handling

**Story Points:** 5

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** QA Engineer / Developer

---

### User Story #8: CI/CD Pipeline

**User Story:**
```
As a developer,
I want to have a CI/CD pipeline,
So that code is automatically tested and built.
```

**Acceptance Criteria:**
- [ ] GitHub Actions workflow runs on push/PR
- [ ] Tests run on multiple Python versions (3.9, 3.10, 3.11)
- [ ] Linting checks are performed
- [ ] Docker image is built and tested
- [ ] Build status badge is visible in README
- [ ] Failed builds send notifications
- [ ] Pipeline completes within 5 minutes

**Story Points:** 5

**Priority:** High

**Sprint:** Sprint 2

**Assigned To:** DevOps Engineer

---

### User Story #9: Docker Containerization

**User Story:**
```
As a developer,
I want to containerize the application,
So that it runs consistently across all environments.
```

**Acceptance Criteria:**
- [ ] Dockerfile builds successfully
- [ ] Container runs the application
- [ ] Application is accessible on port 5000
- [ ] Environment variables are configurable
- [ ] Container includes all dependencies
- [ ] Image size is optimized (< 500MB)
- [ ] Health check endpoint works in container
- [ ] docker-compose.yml is provided

**Story Points:** 3

**Priority:** High

**Sprint:** Sprint 3

**Assigned To:** DevOps Engineer

---

### User Story #10: Application Deployment

**User Story:**
```
As a user,
I want the application to be deployed online,
So that I can access it from anywhere.
```

**Acceptance Criteria:**
- [ ] Application is deployed to cloud platform
- [ ] Application is accessible via public URL
- [ ] HTTPS is enabled
- [ ] Health check endpoint confirms service is running
- [ ] Deployment is automated via CI/CD
- [ ] Application handles traffic without errors
- [ ] Monitoring is configured
- [ ] Backup strategy is in place

**Story Points:** 3

**Priority:** Medium

**Sprint:** Sprint 3

**Assigned To:** DevOps Team

---

## Story Points Reference Guide

| Points | Complexity | Time Estimate | Description |
|--------|-----------|---------------|-------------|
| 1 | Very Small | < 2 hours | Trivial task, well understood |
| 2 | Small | 2-4 hours | Simple, straightforward |
| 3 | Medium | 4-8 hours | Standard complexity, 1 day |
| 5 | Large | 8-16 hours | Complex, 2 days |
| 8 | Very Large | 2-3 days | Needs breakdown |
| 13 | Huge | > 3 days | Must be split into smaller stories |

---

## Priority Levels

| Priority | Indicator | Meaning |
|----------|-----------|---------|
| 🔴 High | Critical | Must complete in current sprint |
| 🟡 Medium | Important | Should complete soon |
| 🟢 Low | Nice to have | Can be deferred |

---

## Definition of Done

A user story is considered "Done" when:

1. ✅ All acceptance criteria are met
2. ✅ Code is written and tested
3. ✅ Unit tests are passing
4. ✅ Code review is completed
5. ✅ Code is merged to main branch
6. ✅ CI/CD pipeline passes
7. ✅ Documentation is updated
8. ✅ Product Owner accepts the story

---

## Template for Creating New Stories

```markdown
### User Story #[NUMBER]: [TITLE]

**User Story:**
As a [user type],
I want to [action],
So that [benefit].

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Story Points:** [1/2/3/5/8]

**Priority:** [High/Medium/Low]

**Sprint:** Sprint [number]

**Assigned To:** [Team member]
```

---

## Notes

- User stories should be written from user's perspective
- Acceptance criteria must be specific and testable
- Story points reflect complexity, not time
- High priority stories should be completed first
- Each story should deliver value independently
- Stories should be small enough to complete in one sprint

---

**For detailed sprint planning, see KANBAN_PLANNING.md**
