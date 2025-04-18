import pytest
from your_module import Manager, Employee, Pod

@pytest.fixture
def manager():
    return Manager("John Doe")

@pytest.fixture
def employee():
    return Employee("Jane Doe")

@pytest.fixture
def pod():
    return Pod("Pod 1")

def test_assign_employee_to_pod(manager, employee, pod):
    manager.assign_employee_to_pod(employee, pod)
    assert employee in pod.employees
    assert pod in employee.pods

def test_assign_employee_to_pod_twice(manager, employee, pod):
    manager.assign_employee_to_pod(employee, pod)
    with pytest.raises(ValueError):
        manager.assign_employee_to_pod(employee, pod)

def test_assign_employee_to_different_pods(manager, employee, pod):
    pod2 = Pod("Pod 2")
    manager.assign_employee_to_pod(employee, pod)
    manager.assign_employee_to_pod(employee, pod2)
    assert employee in pod.employees
    assert employee in pod2.employees
    assert pod in employee.pods
    assert pod2 in employee.pods

def test_assign_none_employee_to_pod(manager, pod):
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod(None, pod)

def test_assign_employee_to_none_pod(manager, employee):
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod(employee, None)