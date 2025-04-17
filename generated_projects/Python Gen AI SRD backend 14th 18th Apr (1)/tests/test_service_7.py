```
import pytest
from your_module import recommend_colleagues

def test_recommend_colleagues_success():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = [{"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Bob Smith"}]
    recommended_colleagues = recommend_colleagues(employee, colleagues)
    assert len(recommended_colleagues) == 2
    assert recommended_colleagues[0]["id"] == 2
    assert recommended_colleagues[1]["id"] == 3

def test_recommend_colleagues_no_colleagues():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = []
    recommended_colleagues = recommend_colleagues(employee, colleagues)
    assert len(recommended_colleagues) == 0

def test_recommend_colleagues_employee_not_found():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = [{"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Bob Smith"}]
    with pytest.raises(ValueError):
        recommend_colleagues({}, colleagues)

def test_recommend_colleagues_colleagues_not_found():
    employee = {"id": 1, "name": "John Doe"}
    with pytest.raises(ValueError):
        recommend_colleagues(employee, [])

def test_recommend_colleagues_employee_in_colleagues():
    employee = {"id": 1, "name": "John Doe"}
    colleagues = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
    recommended_colleagues = recommend_colleagues(employee, colleagues)
    assert len(recommended_colleagues) == 1
    assert recommended_colleagues[0]["id"] == 2
```