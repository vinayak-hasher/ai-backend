```
import pytest
from django.contrib.auth.models import User
from leave_management.models import LeaveRequest

@pytest.mark.django_db
def test_user_can_view_their_leave_requests():
    user = User.objects.create_user('test_user', 'test@example.com', 'password123')
    leave_request1 = LeaveRequest.objects.create(user=user, status='granted')
    leave_request2 = LeaveRequest.objects.create(user=user, status='pending')
    leave_request3 = LeaveRequest.objects.create(user=User.objects.create_user('other_user', 'other@example.com', 'password123'), status='granted')

    assert user.leave_requests.count() == 2
    assert user.leave_requests.filter(status='granted').count() == 1
    assert user.leave_requests.filter(status='pending').count() == 1
    assert leave_request3 not in user.leave_requests.all()
```