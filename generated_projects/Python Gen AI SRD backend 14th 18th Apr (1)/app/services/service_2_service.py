from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class LeaveRequest(BaseModel):
    id: int
    employee: str
    start_date: str
    end_date: str
    leave_type: str
    status: str = "Pending"
    comments: str = ""

class Manager(BaseModel):
    id: int
    name: str
    email: str

leave_requests = []
managers = []

@app.post("/leave-requests/")
def create_leave_request(leave_request: LeaveRequest):
    leave_request.id = len(leave_requests) + 1
    leave_requests.append(leave_request)
    return leave_request

@app.post("/managers/")
def create_manager(manager: Manager):
    manager.id = len(managers) + 1
    managers.append(manager)
    return manager

def get_leave_request(id: int):
    for leave_request in leave_requests:
        if leave_request.id == id:
            return leave_request
    return None

def get_manager(id: int):
    for manager in managers:
        if manager.id == id:
            return manager
    return None

class LeaveRequestService:
    def approve(self, leave_request_id: int, manager_id: int, comments: str):
        leave_request = get_leave_request(leave_request_id)
        manager = get_manager(manager_id)
        if leave_request and manager:
            leave_request.status = "Approved"
            leave_request.comments = comments
            return leave_request
        return None

    def reject(self, leave_request_id: int, manager_id: int, comments: str):
        leave_request = get_leave_request(leave_request_id)
        manager = get_manager(manager_id)
        if leave_request and manager:
            leave_request.status = "Rejected"
            leave_request.comments = comments
            return leave_request
        return None

leave_request_service = LeaveRequestService()

from your_app.models import LeaveRequest, Manager