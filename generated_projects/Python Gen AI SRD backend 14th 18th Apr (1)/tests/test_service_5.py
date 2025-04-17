```
import pytest
from your_module import Manager, Employee, Pod

@pytest.fixture
def setup_data():
    manager = Manager("John Doe")
    employee1 = Employee("Jane Doe")
    employee2 = Employee("Bob Smith")
    pod = Pod("Pod 1")
    return manager, employee1, employee2, pod

def test_assign_employee_to_pod(setup_data):
    manager, employee1, _, pod = setup_data
    manager.assign_employee_to_pod(employee1, pod)
    assert employee1 in pod.employees
    assert pod in employee1.pods

def test_assign_multiple_employees_to_pod(setup_data):
    manager, employee1, employee2, pod = setup_data
    manager.assign_employee_to_pod(employee1, pod)
    manager.assign_employee_to_pod(employee2, pod)
    assert employee1 in pod.employees
    assert employee2 in pod.employees
    assert pod in employee1.pods
    assert pod in employee2.pods

def test_assign_employee_to_multiple_pods(setup_data):
    manager, employee, _, pod1 = setup_data
    pod2 = Pod("Pod 2")
    manager.assign_employee_to_pod(employee, pod1)
    manager.assign_employee_to_pod(employee, pod2)
    assert employee in pod1.employees
    assert employee in pod2.employees
    assert pod1 in employee.pods
    assert pod2 in employee.pods

def test_assign_employee_to_pod_without_manager_rights():
    employee = Employee("Jane Doe")
    pod = Pod("Pod 1")
    with pytest.raises(PermissionError):
        employee.assign_employee_to_pod(employee, pod)

def test_assign_employee_to_pod_with_invalid_input():
    manager = Manager("John Doe")
    employee = Employee("Jane Doe")
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod(employee, "Invalid Pod")
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod("Invalid Employee", Pod("Pod 1"))
```