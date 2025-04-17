```
import pytest
from your_module import get_team_leave_history

@pytest.mark.parametrize("user_role, expected", [
    ("manager", True),
    ("team_member", False),
    ("admin", False),
    (None, False),
])
def test_get_team_leave_history(user_role, expected):
    user = {"role": user_role}
    result = get_team_leave_history(user)
    assert result == expected

def test_get_team_leave_history_no_user():
    result = get_team_leave_history(None)
    assert result == False

def test_get_team_leave_history_empty_user():
    result = get_team_leave_history({})
    assert result == False
```