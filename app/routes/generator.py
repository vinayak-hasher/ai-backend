from fastapi import APIRouter
from app.langgraph_nodes.project_generator import generate_fastapi_project

router = APIRouter()

@router.get("/generate-project/")
def generate_from_analysis(name: str,analysis:dict):
    result = generate_fastapi_project(name,analysis)
    return {"message": result}