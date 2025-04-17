```
import pytest
from django.contrib.auth.models import User
from leave_management.models import LeaveRequest
from leave_management.views import view_leave_requests

@pytest.mark.django_db
def test_view_leave_requests():
    user = User.objects.create_user(username='test_user', password='password')
    leave_request1 = LeaveRequest.objects.create(user=user, status='granted')
    leave_request2 = LeaveRequest.objects.create(user=user, status='pending')
    leave_request3 = LeaveRequest.objects.create(user=User.objects.create_user(username='other_user', password='password'), status='granted')

    response = view_leave_requests(user)

    assert len(response) == 2
    assert leave_request1 in response
    assert leave_request2 in response
    assert leave_request3 not in response
```