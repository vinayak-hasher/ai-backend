from fastapi import FastAPI
from app.routes import analyze,generator

app=FastAPI()
app.include_router(analyze.router)
app.include_router(generator.router)