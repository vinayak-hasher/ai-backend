**HRMS Backend API**
=====================

**Tech Stack**
-------------

* FastAPI
* Python 3.9
* SQLAlchemy
* PostgreSQL

**Installation and Running**
---------------------------

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Folder Structure**
-------------------

```
.
app
main.py
models
__init__.py
user.py
leave.py
pod.py
...
routers
__init__.py
dashboard.py
lms.py
pods.py
auth.py
...
schemas
__init__.py
user.py
leave.py
pod.py
...
tests
__init__.py
test_dashboard.py
test_lms.py
test_pods.py
test_auth.py
...
requirements.txt
README.md
```

**API Endpoints**
----------------

### Dashboard

* `GET /api/dashboard/tiles` - Fetch Dashboard Data

### Leave Management System (LMS)

* `POST /api/lms/leaves/apply` - Apply for Leave
* `GET /api/lms/leaves/status` - Retrieve Leave Status
* `PATCH /api/lms/leaves/{leave_id}/approve` - Approve/Reject Leave (Manager Only)

### Pods

* `POST /api/pods/assign` - Assign Employee to Pod
* `GET /api/pods/{pod_id}/details` - Get Pod Details
* `POST /api/pods/{pod_id}/recommend` - Recommend an Employee for a Pod

### Authentication

* `POST /api/auth/login` - User Login
* `GET /api/auth/user` - Fetch Current User Details

**Authentication Info**
---------------------

### Roles

* `general_user`
* `manager`

### Login Mechanisms

* `email_password`

### Role-Based Access Control (RBAC)

* `general_user`: `apply_for_leave`, `view_leave_status`, `view_assigned_pod`
* `manager`: `approve_reject_leave`, `assign_employee_to_pod`, `view_pod_members`

**Testing Instructions**
----------------------

### Run tests

```
pytest
```

### Test Coverage

* Unit tests for each API endpoint
* Integration tests for business logic rules

**Business Logic Rules**
-----------------------

* A user can apply for leave with a specific category.
* A manager can approve or reject a leave request with comments.
* A manager can assign employees to specific pods.
* An employee can view assigned pod and recommend colleagues for inclusion.