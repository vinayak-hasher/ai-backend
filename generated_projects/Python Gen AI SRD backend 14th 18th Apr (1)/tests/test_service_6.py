```
def test_employee_can_view_assigned_pod():
    # Setup
    employee = EmployeeFactory.create()
    pod = PodFactory.create(employees=[employee])

    # Act
    viewable_pods = employee.viewable_pods

    # Assert
    assert pod in viewable_pods

def test_employee_cannot_view_unassigned_pod():
    # Setup
    employee = EmployeeFactory.create()
    pod = PodFactory.create()

    # Act
    viewable_pods = employee.viewable_pods

    # Assert
    assert pod not in viewable_pods

def test_employee_can_view_multiple_assigned_pods():
    # Setup
    employee = EmployeeFactory.create()
    pod1 = PodFactory.create(employees=[employee])
    pod2 = PodFactory.create(employees=[employee])

    # Act
    viewable_pods = employee.viewable_pods

    # Assert
    assert pod1 in viewable_pods
    assert pod2 in viewable_pods

def test_employee_with_no_assigned_pods_returns_empty_list():
    # Setup
    employee = EmployeeFactory.create()

    # Act
    viewable_pods = employee.viewable_pods

    # Assert
    assert viewable_pods == []
```