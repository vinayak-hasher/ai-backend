```
import pytest
from leave_application.models import LeaveApplication
from users.models import User
from categories.models import Category

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', email='test@example.com', password='password')

@pytest.fixture
def category():
    return Category.objects.create(name='Annual Leave')

def test_apply_leave_with_category(user, category):
    leave_application = LeaveApplication.objects.create(user=user, category=category, start_date='2023-01-01', end_date='2023-01-05')
    assert leave_application.user == user
    assert leave_application.category == category
    assert leave_application.start_date == '2023-01-01'
    assert leave_application.end_date == '2023-01-05'

def test_apply_leave_without_category(user):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, start_date='2023-01-01', end_date='2023-01-05')

def test_apply_leave_with_invalid_category(user):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category='Invalid Category', start_date='2023-01-01', end_date='2023-01-05')

def test_apply_leave_with_invalid_dates(user, category):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=category, start_date='2023-01-05', end_date='2023-01-01')
```