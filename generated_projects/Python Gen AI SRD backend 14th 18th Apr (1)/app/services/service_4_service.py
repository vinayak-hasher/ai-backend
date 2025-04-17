```
def assign_employee_to_pod(manager, employee, pod):
    if not manager or not isinstance(manager, str):
        raise ValueError("Manager is required and must be a string")
    if not employee or not isinstance(employee, str):
        raise ValueError("Employee is required and must be a string")
    if not pod or not isinstance(pod, str):
        raise ValueError("Pod is required and must be a string")
    return f"{employee} assigned to {pod} by {manager}"
```