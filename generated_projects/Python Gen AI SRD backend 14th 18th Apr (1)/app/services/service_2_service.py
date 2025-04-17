```
from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    id: int
    name: str

class LeaveRequest(BaseModel):
    employee_id: int
    start_date: str
    end_date: str
    status: str = 'pending'
    comments: str = ''

class Manager(Employee):
    pass

class LeaveRequestService:
    def approve(self, leave_request: LeaveRequest, manager: Manager, comments: str) -> LeaveRequest:
        if not comments:
            raise ValueError("Comments cannot be empty")
        if not isinstance(manager, Manager):
            raise PermissionError("Only managers can approve leave requests")
        leave_request.status = 'approved'
        leave_request.comments = comments
        return leave_request

    def reject(self, leave_request: LeaveRequest, manager: Manager, comments: str) -> LeaveRequest:
        if not comments:
            raise ValueError("Comments cannot be empty")
        if not isinstance(manager, Manager):
            raise PermissionError("Only managers can reject leave requests")
        leave_request.status = 'rejected'
        leave_request.comments = comments
        return leave_request
```