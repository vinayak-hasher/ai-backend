from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router= APIRouter()

@router.get("/download-project/{project_name}")
def download_zip(project_name:str):
    zip_path=f"generated_projects/{project_name}.zip"
    if os.path.exists(zip_path):
        return FileResponse(zip_path,filename=f"{project_name}.zip", media_type='application/zip')
    return{"error": "Zip not found"}