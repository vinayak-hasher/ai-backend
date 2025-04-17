```
import pytest
from my_app import api_access

@pytest.mark.parametrize("role, endpoint, expected", [
    ("admin", "/admin-only", True),
    ("moderator", "/admin-only", False),
    ("user", "/user-only", True),
    ("user", "/admin-only", False),
    ("guest", "/guest-only", True),
    ("guest", "/user-only", False),
    (None, "/guest-only", False),
])
def test_api_access(role, endpoint, expected):
    assert api_access(role, endpoint) == expected
```