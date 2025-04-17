```
from fastapi import FastAPI

app = FastAPI()

def get_team_leave_history(user_role: str) -> bool:
    if user_role is None:
        raise TypeError("User role cannot be None")
    if user_role not in ["manager", "team_member", "admin"]:
        raise ValueError("Invalid user role")
    return user_role == "manager"
```