```
import pytest
from leave_management.models import LeaveCategory, LeaveApplication
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create_user('testuser', 'testuser@example.com', 'password123')

@pytest.fixture
def leave_category():
    return LeaveCategory.objects.create(name='Annual Leave')

def test_apply_leave_with_category(user, leave_category):
    leave_application = LeaveApplication.objects.create(user=user, category=leave_category, start_date='2022-01-01', end_date='2022-01-05')
    assert leave_application.category == leave_category

def test_apply_leave_without_category(user):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=None, start_date='2022-01-01', end_date='2022-01-05')

def test_apply_leave_with_invalid_category(user):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category='Invalid Category', start_date='2022-01-01', end_date='2022-01-05')
```