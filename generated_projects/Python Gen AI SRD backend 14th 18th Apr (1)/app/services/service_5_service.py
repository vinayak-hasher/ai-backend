```
from typing import Optional

def api_access(role: Optional[str], endpoint: str) -> bool:
    access_control = {
        "/admin-only": ["admin"],
        "/moderator-only": ["moderator", "admin"],
        "/user-only": ["user", "moderator", "admin"],
        "/guest-only": ["guest", "user", "moderator", "admin"],
    }

    if endpoint not in access_control:
        return False

    if role is None:
        return endpoint == "/guest-only"

    return role in access_control.get(endpoint, []) or role is None and endpoint == "/guest-only"
```