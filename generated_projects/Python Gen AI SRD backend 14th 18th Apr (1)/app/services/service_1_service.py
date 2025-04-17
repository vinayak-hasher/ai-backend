```
from fastapi import HTTPException
from leave_application.models import LeaveApplication
from users.models import User
from categories.models import Category

class LeaveApplicationService:
    def apply_leave(self, user: User, category: Category, start_date: str, end_date: str) -> LeaveApplication:
        if not category.is_valid:
            raise HTTPException(status_code=400, detail="Invalid category")
        
        if LeaveApplication.objects.filter(user=user, category=category).exists():
            raise HTTPException(status_code=400, detail="Leave application with same category already exists")
        
        return LeaveApplication.objects.create(user=user, category=category, start_date=start_date, end_date=end_date)

    def apply_leave_without_category(self, user: User, start_date: str, end_date: str) -> None:
        raise HTTPException(status_code=400, detail="Category is required")
```