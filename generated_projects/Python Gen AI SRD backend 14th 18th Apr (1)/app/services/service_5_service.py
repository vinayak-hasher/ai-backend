Here is the corrected Python code:

```
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_token(token: str = Security(oauth2_scheme)):
    if token == "admin_token":
        return "admin"
    elif token == "user_token":
        return "user"
    else:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/api/admin_only")
def admin_only(token: str = Security(oauth2_scheme)):
    user = authenticate_token(token)
    if user == "admin":
        return {"message": "Admin access granted"}
    elif user == "user":
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
```