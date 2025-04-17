Here is the corrected Python code:

```
from pydantic import BaseModel
from typing import Optional

class Manager(BaseModel):
    id: int
    name: str

class LeaveRequest(BaseModel):
    employee_id: int
    start_date: str
    end_date: str
    status: str = "Pending"
    comment: Optional[str] = None

    def approve(self, manager: Manager, comment: str):
        if manager.id != 1:
            raise PermissionError("Only manager with id 1 can approve/reject leave requests")
        if not comment:
            raise ValueError("Comment cannot be empty")
        self.status = "Approved"
        self.comment = comment

    def reject(self, manager: Manager, comment: str):
        if manager.id != 1:
            raise PermissionError("Only manager with id 1 can approve/reject leave requests")
        if not comment:
            raise ValueError("Comment cannot be empty")
        self.status = "Rejected"
        self.comment = comment
```