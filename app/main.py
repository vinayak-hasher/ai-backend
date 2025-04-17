from fastapi import FastAPI
from app.routes import analyze
from app.routes import zip_download

app=FastAPI()
app.include_router(analyze.router)
