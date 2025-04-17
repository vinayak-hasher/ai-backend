```
import pytest
from your_module import recommend_colleague

def test_recommend_colleague_success():
    employee = {"id": 1, "name": "John Doe"}
    colleague = {"id": 2, "name": "Jane Doe"}
    pod = {"id": 1, "name": "Pod 1"}
    assert recommend_colleague(employee, colleague, pod) == {"message": "Colleague recommended successfully"}

def test_recommend_colleague_employee_not_found():
    employee = {"id": 1, "name": "John Doe"}
    colleague = {"id": 2, "name": "Jane Doe"}
    pod = {"id": 1, "name": "Pod 1"}
    with pytest.raises(ValueError):
        recommend_colleague({"id": 3, "name": "Unknown Employee"}, colleague, pod)

def test_recommend_colleague_colleague_not_found():
    employee = {"id": 1, "name": "John Doe"}
    pod = {"id": 1, "name": "Pod 1"}
    with pytest.raises(ValueError):
        recommend_colleague(employee, {"id": 3, "name": "Unknown Colleague"}, pod)

def test_recommend_colleague_pod_not_found():
    employee = {"id": 1, "name": "John Doe"}
    colleague = {"id": 2, "name": "Jane Doe"}
    with pytest.raises(ValueError):
        recommend_colleague(employee, colleague, {"id": 3, "name": "Unknown Pod"})

def test_recommend_colleague_same_employee_and_colleague():
    employee = {"id": 1, "name": "John Doe"}
    pod = {"id": 1, "name": "Pod 1"}
    with pytest.raises(ValueError):
        recommend_colleague(employee, employee, pod)

def test_recommend_colleague_already_recommended():
    employee = {"id": 1, "name": "John Doe"}
    colleague = {"id": 2, "name": "Jane Doe"}
    pod = {"id": 1, "name": "Pod 1"}
    recommend_colleague(employee, colleague, pod)
    with pytest.raises(ValueError):
        recommend_colleague(employee, colleague, pod)
```