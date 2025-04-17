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
    # assuming get_team_leave_history function takes user_role as an argument
    result = get_team_leave_history(user_role)
    assert result == expected

def test_get_team_leave_history_with_invalid_input():
    with pytest.raises(ValueError):
        get_team_leave_history("invalid_role")

def test_get_team_leave_history_with_no_input():
    with pytest.raises(TypeError):
        get_team_leave_history()
```