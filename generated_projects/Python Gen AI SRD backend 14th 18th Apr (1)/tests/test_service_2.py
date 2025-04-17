```
import pytest
from your_app.models import LeaveRequest
from your_app.views import approve_leave_request, reject_leave_request

@pytest.fixture
def leave_request():
    return LeaveRequest.objects.create(employee='John Doe', start_date='2022-01-01', end_date='2022-01-05', reason='Vacation')

def test_approve_leave_request(leave_request):
    approve_leave_request(leave_request.id, 'Approved')
    leave_request.refresh_from_db()
    assert leave_request.status == 'Approved'
    assert leave_request.comments == 'Approved'

def test_reject_leave_request(leave_request):
    reject_leave_request(leave_request.id, 'Rejected')
    leave_request.refresh_from_db()
    assert leave_request.status == 'Rejected'
    assert leave_request.comments == 'Rejected'

def test_approve_leave_request_without_comments(leave_request):
    approve_leave_request(leave_request.id, '')
    leave_request.refresh_from_db()
    assert leave_request.status == 'Approved'
    assert leave_request.comments == ''

def test_reject_leave_request_without_comments(leave_request):
    reject_leave_request(leave_request.id, '')
    leave_request.refresh_from_db()
    assert leave_request.status == 'Rejected'
    assert leave_request.comments == ''

def test_approve_non_existent_leave_request():
    with pytest.raises(LeaveRequest.DoesNotExist):
        approve_leave_request(999, 'Approved')

def test_reject_non_existent_leave_request():
    with pytest.raises(LeaveRequest.DoesNotExist):
        reject_leave_request(999, 'Rejected')
```