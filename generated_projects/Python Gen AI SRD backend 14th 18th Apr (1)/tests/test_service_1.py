```
import pytest
from datetime import datetime, timedelta
from your_module import apply_for_leave  # replace with your actual module

def test_apply_for_leave_valid_dates():
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=5)
    assert apply_for_leave(start_date, end_date) == "Leave applied successfully"

def test_apply_for_leave_invalid_start_date():
    start_date = datetime.now().date() - timedelta(days=5)
    end_date = datetime.now().date() + timedelta(days=5)
    with pytest.raises(ValueError):
        apply_for_leave(start_date, end_date)

def test_apply_for_leave_invalid_end_date():
    start_date = datetime.now().date()
    end_date = start_date - timedelta(days=5)
    with pytest.raises(ValueError):
        apply_for_leave(start_date, end_date)

def test_apply_for_leave_same_dates():
    date = datetime.now().date()
    with pytest.raises(ValueError):
        apply_for_leave(date, date)

def test_apply_for_leave_start_date_greater_than_end_date():
    start_date = datetime.now().date() + timedelta(days=5)
    end_date = datetime.now().date()
    with pytest.raises(ValueError):
        apply_for_leave(start_date, end_date)
```