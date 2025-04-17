```
from fastapi import HTTPException
from leave_application.models import LeaveApplication
from users.models import User
from categories.models import Category

class LeaveApplicationService:
    def apply_leave(self, user: User, category: Category, start_date: str, end_date: str) -> LeaveApplication:
        if not category:
            raise ValueError("Category is required")
        if start_date >= end_date:
            raise ValueError("Start date cannot be greater than or equal to end date")
        if not isinstance(category, Category):
            raise ValueError("Invalid category")
        return LeaveApplication.objects.create(user=user, category=category, start_date=start_date, end_date=end_date)
```