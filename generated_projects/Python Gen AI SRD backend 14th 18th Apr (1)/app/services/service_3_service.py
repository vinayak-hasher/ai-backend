```
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.base import SecurityBase
from fastapi import FastAPI
from typing import List
from django.contrib.auth.models import User
from leave_management.models import LeaveRequest

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = User.objects.get(username=token)
    return user

@app.get("/leave_requests/")
async def read_leave_requests(user: User = Depends(get_current_user)):
    leave_requests = user.leave_requests.all()
    return [{"id": lr.id, "status": lr.status} for lr in leave_requests]

@app.get("/leave_requests/{status}")
async def read_leave_requests_by_status(status: str, user: User = Depends(get_current_user)):
    leave_requests = user.leave_requests.filter(status=status)
    return [{"id": lr.id, "status": lr.status} for lr in leave_requests]
```