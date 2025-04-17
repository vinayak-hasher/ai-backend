Here is the corrected Python code:

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class User:
    def __init__(self, id: int):
        self.id = id

class Pod:
    def __init__(self, id: int, assigned_to: Optional[User] = None):
        self.id = id
        self.assigned_to = assigned_to

class PodResponse(BaseModel):
    id: int

class RecommendResponse(BaseModel):
    recommended_colleagues: List[int]

pods = {}

@app.get("/pods/{pod_id}")
def get_pod(pod_id: int):
    pod = pods.get(pod_id)
    if pod is None:
        raise HTTPException(status_code=404)
    if pod.assigned_to is None or pod.assigned_to.id != 1:  # Replace with actual user authentication logic
        raise HTTPException(status_code=403)
    return PodResponse(id=pod.id)

@app.post("/pods/{pod_id}/recommend")
def recommend_colleagues(pod_id: int, json_data: dict):
    user_ids = json_data.get('user_ids')
    if not isinstance(user_ids, list):
        raise HTTPException(status_code=400)
    for user_id in user_ids:
        if not isinstance(user_id, int):
            raise HTTPException(status_code=400)
    pod = pods.get(pod_id)
    if pod is None:
        raise HTTPException(status_code=404)
    if pod.assigned_to is None or pod.assigned_to.id != 1:  # Replace with actual user authentication logic
        raise HTTPException(status_code=403)
    return RecommendResponse(recommended_colleagues=user_ids)

def create_pod(id: int, assigned_to: User):
    pods[id] = Pod(id, assigned_to)
    return pods[id]

def create_user(id: int):
    return User(id)

# Initialize pods and users for testing
create_pod(1, create_user(1))
create_user(2)
create_user(3)
```