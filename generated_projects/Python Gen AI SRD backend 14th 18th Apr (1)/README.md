**HRMS Backend API**
=====================

**Tech Stack**
-------------

* Python 3.9
* FastAPI 0.70.0
* SQLAlchemy 1.4.25
* Pydantic 1.9.0
* Alembic 1.7.5

**Installation and Running**
---------------------------

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
uvicorn main:app --reload
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
pod.py
leave.py
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
pod.py
leave.py
...
tests
__init__.py
test_dashboard.py
test_lms.py
test_pods.py
test_auth.py
...
alembic.ini
requirements.txt
README.md
```

**API Endpoints**
----------------

### Dashboard

* `GET /api/dashboard/tiles`: Fetch Dashboard Data

### Leave Management System (LMS)

* `POST /api/lms/leaves/apply`: Apply for Leave
* `GET /api/lms/leaves/status`: Retrieve Leave Status
* `PATCH /api/lms/leaves/{leave_id}/approve`: Approve/Reject Leave (Manager Only)

### Pods

* `POST /api/pods/assign`: Assign Employee to Pod
* `GET /api/pods/{pod_id}/details`: Get Pod Details
* `POST /api/pods/{pod_id}/recommend`: Recommend an Employee for a Pod

### Authentication

* `POST /api/auth/login`: User Login
* `GET /api/auth/user`: Fetch Current User Details

**Business Logic Rules**
-------------------------

* A user can apply for leave with a valid start and end date.
* A manager can approve or reject a leave request with a comment.
* A user can view their assigned pod and recommend colleagues for inclusion.
* A manager can assign employees to specific pods.
* The system enforces Role-Based Access Control (RBAC) for API access.

**Auth System**
-------------

* Roles: `manager`, `employee`
* Login Mechanisms: `email`, `password`
* RBAC:
	+ `manager`: `lms`, `pods`
	+ `employee`: `lms`

**Testing Instructions**
-----------------------

### Run tests

```
pytest
```

### Run tests with coverage

```
pytest --cov=app
```