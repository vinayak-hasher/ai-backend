```
import pytest
from your_module import assign_employee_to_pod

def test_assign_employee_to_pod_success():
    manager = "John Doe"
    employee = "Jane Doe"
    pod = "Pod 1"
    assert assign_employee_to_pod(manager, employee, pod) == f"{employee} assigned to {pod} by {manager}"

def test_assign_employee_to_pod_no_manager():
    employee = "Jane Doe"
    pod = "Pod 1"
    with pytest.raises(ValueError):
        assign_employee_to_pod(None, employee, pod)

def test_assign_employee_to_pod_no_employee():
    manager = "John Doe"
    pod = "Pod 1"
    with pytest.raises(ValueError):
        assign_employee_to_pod(manager, None, pod)

def test_assign_employee_to_pod_no_pod():
    manager = "John Doe"
    employee = "Jane Doe"
    with pytest.raises(ValueError):
        assign_employee_to_pod(manager, employee, None)
```