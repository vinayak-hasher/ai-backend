```
from fastapi import HTTPException
from your_app.models import LeaveRequest

def approve_leave_request(leave_request_id: int, comments: str):
    try:
        leave_request = LeaveRequest.objects.get(id=leave_request_id)
        leave_request.status = 'Approved'
        leave_request.comments = comments
        leave_request.save()
        return leave_request
    except LeaveRequest.DoesNotExist:
        raise HTTPException(status_code=404, detail="Leave request not found")

def reject_leave_request(leave_request_id: int, comments: str):
    try:
        leave_request = LeaveRequest.objects.get(id=leave_request_id)
        leave_request.status = 'Rejected'
        leave_request.comments = comments
        leave_request.save()
        return leave_request
    except LeaveRequest.DoesNotExist:
        raise HTTPException(status_code=404, detail="Leave request not found")
```