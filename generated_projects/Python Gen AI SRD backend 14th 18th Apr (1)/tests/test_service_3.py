```
import pytest
from django.contrib.auth.models import User
from leave_request.models import LeaveRequest

@pytest.mark.django_db
def test_user_can_view_their_leave_requests():
    user = User.objects.create_user('test_user', 'test@example.com', 'password123')
    leave_request1 = LeaveRequest.objects.create(user=user, status='granted')
    leave_request2 = LeaveRequest.objects.create(user=user, status='pending')
    leave_request3 = LeaveRequest.objects.create(user=User.objects.create_user('another_user', 'another@example.com', 'password123'), status='granted')

    assert user.leave_request_set.filter(status__in=['granted', 'pending']).count() == 2
    assert user.leave_request_set.filter(status='granted').first() == leave_request1
    assert user.leave_request_set.filter(status='pending').first() == leave_request2
    assert leave_request3 not in user.leave_request_set.all()
```