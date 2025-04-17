```
import pytest
from your_module import LeaveRequest, Manager

@pytest.fixture
def leave_request():
    return LeaveRequest(employee_id=1, start_date="2022-01-01", end_date="2022-01-05")

@pytest.fixture
def manager():
    return Manager(id=1, name="John Doe")

def test_approve_leave_request(manager, leave_request):
    leave_request.approve(manager, "Approved")
    assert leave_request.status == "Approved"
    assert leave_request.comments == "Approved"

def test_reject_leave_request(manager, leave_request):
    leave_request.reject(manager, "Rejected")
    assert leave_request.status == "Rejected"
    assert leave_request.comments == "Rejected"

def test_approve_leave_request_without_comments(manager, leave_request):
    with pytest.raises(ValueError):
        leave_request.approve(manager, "")

def test_reject_leave_request_without_comments(manager, leave_request):
    with pytest.raises(ValueError):
        leave_request.reject(manager, "")

def test_approve_leave_request_with_empty_manager(manager, leave_request):
    with pytest.raises(ValueError):
        leave_request.approve(None, "Approved")

def test_reject_leave_request_with_empty_manager(manager, leave_request):
    with pytest.raises(ValueError):
        leave_request.reject(None, "Rejected")
```