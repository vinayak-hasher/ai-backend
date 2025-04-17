Here is the corrected Python code:

```
from datetime import datetime, timedelta

def apply_for_leave(start_date, end_date):
    if start_date < datetime.now().date():
        raise ValueError("Start date cannot be in the past")
    if end_date < start_date:
        raise ValueError("End date cannot be before start date")
    if start_date == end_date:
        raise ValueError("Start and end dates cannot be the same")
    return "Leave applied successfully"
```