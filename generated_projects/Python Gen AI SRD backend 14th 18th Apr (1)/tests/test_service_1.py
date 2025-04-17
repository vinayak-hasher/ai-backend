```
import pytest
from your_module import apply_for_leave

@pytest.mark.parametrize("employee_id, leave_category, expected", [
    (1, "annual", {"employee_id": 1, "leave_category": "annual", "status": "pending"}),
    (2, "sick", {"employee_id": 2, "leave_category": "sick", "status": "pending"}),
    (3, "maternity", {"employee_id": 3, "leave_category": "maternity", "status": "pending"}),
    (4, "paternity", {"employee_id": 4, "leave_category": "paternity", "status": "pending"}),
    (5, None, {"error": "Leave category is required"}),
    (6, "", {"error": "Leave category is required"}),
    (7, "unknown", {"error": "Invalid leave category"}),
])
def test_apply_for_leave(employee_id, leave_category, expected):
    result = apply_for_leave(employee_id, leave_category)
    assert result == expected
```