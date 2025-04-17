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
    # Assume get_user_role function returns the user's role
    def get_user_role():
        return user_role

    result = get_team_leave_history(get_user_role)
    assert result == expected

def test_get_team_leave_history_no_user_role():
    def get_user_role():
        return None

    with pytest.raises(ValueError):
        get_team_leave_history(get_user_role)
```