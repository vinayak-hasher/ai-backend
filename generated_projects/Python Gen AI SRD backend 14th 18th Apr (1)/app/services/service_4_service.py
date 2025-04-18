from typing import Optional

class Pod:
    def __init__(self, name: str):
        self.name = name

class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.assigned_pod: Optional[Pod] = None

    def assign_pod(self, pod: Pod) -> None:
        self.assigned_pod = pod

    def view_assigned_pod(self) -> Optional[Pod]:
        return self.assigned_pod

    def recommend_colleague(self, colleague: 'Employee') -> str:
        if colleague == self:
            raise ValueError("Cannot recommend self")
        if not self.assigned_pod:
            raise ValueError("Employee must be assigned to a pod to recommend a colleague")
        return f"{colleague.name} recommended successfully"