from fastapi import APIRouter
from app.langgraph_nodes.project_generator import generate_fastapi_project

router = APIRouter()

@router.get("/generate-project/{name}")
def generate(name: str):
    result = generate_fastapi_project(name)
    return {"message": result}