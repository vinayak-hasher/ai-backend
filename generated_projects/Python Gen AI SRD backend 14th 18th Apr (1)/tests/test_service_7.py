```
import pytest
from your_module import recommend_colleagues

def test_recommend_colleagues_success():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = [{"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Bob Smith"}]
    pod = {"id": 1, "name": "Pod 1"}
    assert recommend_colleagues(employee, colleagues, pod) == {"message": "Colleagues recommended successfully"}

def test_recommend_colleagues_no_colleagues():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = []
    pod = {"id": 1, "name": "Pod 1"}
    assert recommend_colleagues(employee, colleagues, pod) == {"error": "No colleagues to recommend"}

def test_recommend_colleagues_no_pod():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = [{"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Bob Smith"}]
    pod = None
    assert recommend_colleagues(employee, colleagues, pod) == {"error": "Pod not found"}

def test_recommend_colleagues_employee_not_found():
    employee = None
    colleagues = [{"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Bob Smith"}]
    pod = {"id": 1, "name": "Pod 1"}
    assert recommend_colleagues(employee, colleagues, pod) == {"error": "Employee not found"}
```