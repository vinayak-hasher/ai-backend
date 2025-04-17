```
import pytest
from your_app.models import LeaveRequest, Manager

@pytest.fixture
def leave_request():
    return LeaveRequest.objects.create(status='pending')

@pytest.fixture
def manager():
    return Manager.objects.create(username='manager', email='manager@example.com')

def test_manager_can_approve_leave_request_with_comment(leave_request, manager):
    leave_request.approve(manager, 'Approved')
    assert leave_request.status == 'approved'
    assert leave_request.comments == 'Approved'

def test_manager_can_reject_leave_request_with_comment(leave_request, manager):
    leave_request.reject(manager, 'Rejected')
    assert leave_request.status == 'rejected'
    assert leave_request.comments == 'Rejected'

def test_manager_cannot_approve_leave_request_without_comment(leave_request, manager):
    with pytest.raises(ValueError):
        leave_request.approve(manager, '')

def test_manager_cannot_reject_leave_request_without_comment(leave_request, manager):
    with pytest.raises(ValueError):
        leave_request.reject(manager, '')

def test_non_manager_cannot_approve_leave_request(leave_request):
    user = User.objects.create(username='user', email='user@example.com')
    with pytest.raises(PermissionError):
        leave_request.approve(user, 'Approved')

def test_non_manager_cannot_reject_leave_request(leave_request):
    user = User.objects.create(username='user', email='user@example.com')
    with pytest.raises(PermissionError):
        leave_request.reject(user, 'Rejected')
```