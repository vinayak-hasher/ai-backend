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
    leave_application = LeaveApplication.objects.create(user=user, category=category, start_date='2022-01-01', end_date='2022-01-05')
    assert leave_application.category == category

def test_apply_leave_without_category(user):
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, start_date='2022-01-01', end_date='2022-01-05')

def test_apply_leave_with_invalid_category(user):
    invalid_category = Category.objects.create(name='Invalid Category')
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=invalid_category, start_date='2022-01-01', end_date='2022-01-05')

def test_apply_leave_with_same_category_twice(user, category):
    LeaveApplication.objects.create(user=user, category=category, start_date='2022-01-01', end_date='2022-01-05')
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=category, start_date='2022-01-06', end_date='2022-01-10')
```