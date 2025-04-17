Here is the corrected Python code:

```
def apply_for_leave(reason: str, start_date: datetime, end_date: datetime):
    if not reason.strip():  # Check if reason is empty or contains only whitespace
        raise ValueError("Reason cannot be empty")
    if start_date < datetime.now():
        raise ValueError("Start date cannot be in the past")
    if end_date < start_date:
        raise ValueError("End date cannot be before start date")
    if start_date == end_date:
        raise ValueError("Start and end dates cannot be the same")
    return "Leave applied successfully"
```