Here is the corrected code:

```
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Manager(BaseModel):
    id: int
    name: str

class LeaveRequest(BaseModel):
    employee_id: int
    start_date: str
    end_date: str
    status: Optional[str] = None
    comment: Optional[str] = None

    def approve(self, manager: Manager, comment: str):
        if manager.id != 1:
            raise PermissionError("Only manager with id 1 can approve")
        if not comment:
            raise ValueError("Comment cannot be empty")
        self.status = "Approved"
        self.comment = comment

    def reject(self, manager: Manager, comment: str):
        if manager.id != 1:
            raise PermissionError("Only manager with id 1 can reject")
        if not comment:
            raise ValueError("Comment cannot be empty")
        self.status = "Rejected"
        self.comment = comment
```