```
import pytest
from datetime import datetime, timedelta
from your_module import apply_for_leave

def test_apply_for_leave_valid_reason_and_dates():
    reason = "I'm sick"
    start_date = datetime.now()
    end_date = start_date + timedelta(days=3)
    assert apply_for_leave(reason, start_date, end_date) == "Leave applied successfully"

def test_apply_for_leave_invalid_reason():
    reason = ""
    start_date = datetime.now()
    end_date = start_date + timedelta(days=3)
    with pytest.raises(ValueError):
        apply_for_leave(reason, start_date, end_date)

def test_apply_for_leave_invalid_start_date():
    reason = "I'm sick"
    start_date = datetime.now() - timedelta(days=3)
    end_date = start_date + timedelta(days=3)
    with pytest.raises(ValueError):
        apply_for_leave(reason, start_date, end_date)

def test_apply_for_leave_invalid_end_date():
    reason = "I'm sick"
    start_date = datetime.now()
    end_date = start_date - timedelta(days=3)
    with pytest.raises(ValueError):
        apply_for_leave(reason, start_date, end_date)

def test_apply_for_leave_same_dates():
    reason = "I'm sick"
    start_date = datetime.now()
    end_date = start_date
    with pytest.raises(ValueError):
        apply_for_leave(reason, start_date, end_date)
```