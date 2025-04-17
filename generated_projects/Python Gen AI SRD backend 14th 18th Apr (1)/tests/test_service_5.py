```
import pytest
from your_module import assign_employee_to_pod, Pod, Employee

@pytest.fixture
def pod():
    return Pod("Pod 1")

@pytest.fixture
def employee():
    return Employee("John Doe")

def test_assign_employee_to_pod(pod, employee):
    assign_employee_to_pod(pod, employee)
    assert employee.pod == pod
    assert employee in pod.employees

def test_assign_employee_to_pod_twice(pod, employee):
    assign_employee_to_pod(pod, employee)
    with pytest.raises(ValueError):
        assign_employee_to_pod(pod, employee)

def test_assign_employee_to_different_pods(pod, employee):
    pod2 = Pod("Pod 2")
    assign_employee_to_pod(pod, employee)
    assign_employee_to_pod(pod2, employee)
    assert employee.pod == pod2
    assert employee in pod2.employees
    assert employee not in pod.employees

def test_assign_none_to_pod(pod):
    with pytest.raises(TypeError):
        assign_employee_to_pod(pod, None)

def test_assign_employee_to_none(employee):
    with pytest.raises(TypeError):
        assign_employee_to_pod(None, employee)
```