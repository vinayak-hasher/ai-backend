```
from typing import List
from app.models import Employee, Pod

class EmployeeService:
    def __init__(self, employee: Employee):
        self.employee = employee

    @property
    def viewable_pods(self) -> List[Pod]:
        return [pod for pod in Pod.objects.all() if self.employee in pod.employees]
```