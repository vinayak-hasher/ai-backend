from fastapi import FastAPI
from app.routes import analyze,generator
from app.routes import zip_download

app=FastAPI()
app.include_router(analyze.router)
app.include_router(generator.router)
app.include_router(zip_download.router)