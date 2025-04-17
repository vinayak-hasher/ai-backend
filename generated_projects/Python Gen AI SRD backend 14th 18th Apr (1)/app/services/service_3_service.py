Here is the corrected code:

```
from fastapi import Depends
from sqlalchemy.orm import Session
from your_app.models import User, Pod
from your_app.database import get_db

class PodService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def assign_pod_to_user(self, user: User, pod: Pod):
        user.pod = pod
        self.db.add(user)
        self.db.commit()

    def recommend_colleagues_for_pod(self, user: User, pod: Pod, colleague: User):
        if user.pod != pod:
            raise ValueError("User is not assigned to this pod")
        if user.pod is None:
            raise ValueError("User is not assigned to any pod")
        pod.recommended_colleagues.add(colleague)
        self.db.add(pod)
        self.db.commit()
```