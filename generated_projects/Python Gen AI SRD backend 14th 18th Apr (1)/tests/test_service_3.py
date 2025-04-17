```
import pytest
from your_app.models import Employee, LeaveRequest

@pytest.fixture
def employee():
    return Employee.objects.create_user('test@example.com', 'password123')

@pytest.fixture
def leave_request(employee):
    return LeaveRequest.objects.create(employee=employee, status='pending')

def test_employee_can_view_granted_leave_request(employee):
    granted_request = LeaveRequest.objects.create(employee=employee, status='granted')
    assert employee.leave_requests.filter(status='granted').exists()

def test_employee_can_view_pending_leave_request(employee, leave_request):
    assert employee.leave_requests.filter(status='pending').exists()

def test_employee_cannot_view_others_leave_request(employee, leave_request):
    other_employee = Employee.objects.create_user('other@example.com', 'password123')
    assert not other_employee.leave_requests.filter(status='pending').exists()

def test_employee_cannot_view_deleted_leave_request(employee):
    deleted_request = LeaveRequest.objects.create(employee=employee, status='pending', deleted_at='2022-01-01')
    assert not employee.leave_requests.filter(status='pending').exists()
```