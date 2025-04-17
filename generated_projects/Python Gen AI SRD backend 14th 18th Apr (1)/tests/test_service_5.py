```
def test_assign_employee_to_pod():
    manager = Manager()
    employee = Employee()
    pod = Pod()

    # Happy path
    manager.assign_employee_to_pod(employee, pod)
    assert employee.pod == pod
    assert pod.employees == [employee]

    # Edge case: Assign same employee to same pod
    manager.assign_employee_to_pod(employee, pod)
    assert employee.pod == pod
    assert len(pod.employees) == 1

    # Edge case: Assign same employee to different pod
    new_pod = Pod()
    manager.assign_employee_to_pod(employee, new_pod)
    assert employee.pod == new_pod
    assert len(new_pod.employees) == 1
    assert pod.employees == []

    # Edge case: Assign None employee
    with pytest.raises(ValueError):
        manager.assign_employee_to_pod(None, pod)

    # Edge case: Assign None pod
    with pytest.raises(ValueError):
        manager.assign_employee_to_pod(employee, None)
```