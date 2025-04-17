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
__init__.py
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
utils
__init__.py
auth_utils.py
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
* `POST /api/pods/{pod_id}/recommend`: Recommend Employee for Pod

### Authentication

* `POST /api/auth/login`: User Login
* `GET /api/auth/user`: Fetch Current User Details

**Authentication Info**
-----------------------

### Roles

* `general_user`
* `manager`

### Login Mechanisms

* `email_password`

### Role-Based Access Control (RBAC)

* `general_user`: `apply_for_leave`, `view_leave_status`, `view_assigned_pod`
* `manager`: `approve_reject_leave`, `access_leave_reports`, `assign_employees_to_pods`

**Testing Instructions**
-----------------------

### Run tests

```
pytest
```

### Coverage report

```
pytest --cov=app
```