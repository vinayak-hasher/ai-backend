```
def test_assign_employee_to_pod_success(manager, employee, pod):
    # Arrange
    manager.assign_employee_to_pod(employee, pod)

    # Assert
    assert employee in pod.employees
    assert pod in employee.pods


def test_assign_employee_to_pod_already_assigned(manager, employee, pod):
    # Arrange
    manager.assign_employee_to_pod(employee, pod)
    with pytest.raises(ValueError):
        manager.assign_employee_to_pod(employee, pod)


def test_assign_employee_to_pod_employee_none(manager, pod):
    # Arrange
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod(None, pod)


def test_assign_employee_to_pod_pod_none(manager, employee):
    # Arrange
    with pytest.raises(TypeError):
        manager.assign_employee_to_pod(employee, None)
```