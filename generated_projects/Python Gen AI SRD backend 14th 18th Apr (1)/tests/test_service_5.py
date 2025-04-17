```
import pytest
from your_module import assign_employee_to_pod

@pytest.fixture
def manager():
    return Manager()

@pytest.fixture
def employee():
    return Employee()

@pytest.fixture
def pod():
    return Pod()

def test_assign_employee_to_pod(manager, employee, pod):
    assign_employee_to_pod(manager, employee, pod)
    assert employee.pod == pod
    assert employee in pod.employees

def test_assign_employee_to_pod_twice(manager, employee, pod):
    assign_employee_to_pod(manager, employee, pod)
    with pytest.raises(ValueError):
        assign_employee_to_pod(manager, employee, pod)

def test_assign_employee_to_different_pod(manager, employee, pod, another_pod):
    assign_employee_to_pod(manager, employee, pod)
    assign_employee_to_pod(manager, employee, another_pod)
    assert employee.pod == another_pod
    assert employee not in pod.employees
    assert employee in another_pod.employees

def test_assign_employee_without_manager(employee, pod):
    with pytest.raises(ValueError):
        assign_employee_to_pod(None, employee, pod)

def test_assign_employee_without_pod(manager, employee):
    with pytest.raises(ValueError):
        assign_employee_to_pod(manager, employee, None)
```