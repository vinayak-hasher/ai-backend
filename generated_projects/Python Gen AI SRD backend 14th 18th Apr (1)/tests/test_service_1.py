import pytest
from leave_management.models import LeaveCategory, LeaveApplication
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_apply_leave_with_category():
    user = User.objects.create_user('testuser', 'testuser@example.com', 'password123')
    category = LeaveCategory.objects.create(name='Annual Leave')

    # Happy path
    leave_application = LeaveApplication.objects.create(user=user, category=category, start_date='2022-01-01', end_date='2022-01-05')
    assert leave_application.user == user
    assert leave_application.category == category
    assert leave_application.start_date == '2022-01-01'
    assert leave_application.end_date == '2022-01-05'

    # Edge case: User is None
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=None, category=category, start_date='2022-01-01', end_date='2022-01-05')

    # Edge case: Category is None
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=None, start_date='2022-01-01', end_date='2022-01-05')

    # Edge case: Start date is after end date
    with pytest.raises(ValueError):
        LeaveApplication.objects.create(user=user, category=category, start_date='2022-01-05', end_date='2022-01-01')