import pytest
from your_module import Employee, Pod

@pytest.fixture
def employee():
    return Employee("John Doe", "john.doe@example.com")

@pytest.fixture
def pod():
    return Pod("Pod 1")

def test_employee_can_view_assigned_pod(employee, pod):
    employee.assign_pod(pod)
    assert employee.view_assigned_pod() == pod

def test_employee_cannot_view_unassigned_pod(employee):
    assert employee.view_assigned_pod() is None

def test_employee_can_recommend_colleague(employee):
    colleague = Employee("Jane Doe", "jane.doe@example.com")
    assert employee.recommend_colleague(colleague) == "Colleague recommended successfully"

def test_employee_cannot_recommend_self(employee):
    with pytest.raises(ValueError):
        employee.recommend_colleague(employee)

def test_employee_cannot_recommend_colleague_without_pod(employee, pod):
    colleague = Employee("Jane Doe", "jane.doe@example.com")
    with pytest.raises(ValueError):
        employee.recommend_colleague(colleague)
    employee.assign_pod(pod)
    assert employee.recommend_colleague(colleague) == "Colleague recommended successfully"