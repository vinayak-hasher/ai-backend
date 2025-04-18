import pytest
from your_app.models import LeaveRequest, Manager

@pytest.fixture
def leave_request():
    return LeaveRequest.objects.create(employee='John Doe', start_date='2022-01-01', end_date='2022-01-05', leave_type='Annual')

@pytest.fixture
def manager():
    return Manager.objects.create(name='Manager Name', email='manager@example.com')

def test_approve_leave_request(leave_request, manager):
    leave_request.approve(manager, 'Approved')
    assert leave_request.status == 'Approved'
    assert leave_request.comments == 'Approved'

def test_reject_leave_request(leave_request, manager):
    leave_request.reject(manager, 'Rejected')
    assert leave_request.status == 'Rejected'
    assert leave_request.comments == 'Rejected'

def test_approve_leave_request_without_comments(leave_request, manager):
    leave_request.approve(manager, '')
    assert leave_request.status == 'Approved'
    assert leave_request.comments == ''

def test_reject_leave_request_without_comments(leave_request, manager):
    leave_request.reject(manager, '')
    assert leave_request.status == 'Rejected'
    assert leave_request.comments == ''

def test_approve_leave_request_with_long_comments(leave_request, manager):
    long_comment = 'a' * 500
    leave_request.approve(manager, long_comment)
    assert leave_request.status == 'Approved'
    assert leave_request.comments == long_comment

def test_reject_leave_request_with_long_comments(leave_request, manager):
    long_comment = 'a' * 500
    leave_request.reject(manager, long_comment)
    assert leave_request.status == 'Rejected'
    assert leave_request.comments == long_comment