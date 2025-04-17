```
from typing import List

def recommend_colleagues(employee: dict, colleagues: List[dict]) -> List[dict]:
    if employee not in colleagues:
        raise ValueError("Employee is not in the list of colleagues")

    recommended_colleagues = [colleague for colleague in colleagues if colleague != employee]
    return recommended_colleagues
```