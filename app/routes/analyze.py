from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.utils.docx_parser import extract_text_from_docx
from app.langgraph_nodes.srs_analysis import analyze_srs_content
from app.langgraph_nodes.project_generator import generate_fastapi_project
from app.langgraph_nodes.test_generator import generate_unit_tests
from app.langgraph_nodes.code_generator import generate_code_from_tests
from app.utils.zipper import zip_project
from app.langgraph_nodes.documenter import generate_readme,generate_api_docs,generate_mermaid_flow
from app.utils.result_logger import save_result_summary
import os
import json

router = APIRouter()

@router.post("/upload-srs-and-generate")
async def upload_srs_and_generate(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        raise HTTPException(status_code=400, detail="Only .docx files are supported.")

    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    srs_text = extract_text_from_docx(file_path)
    analysis_result=analyze_srs_content(srs_text)

    project_name = file.filename.replace(".docx", "")
    project_path=f"generated_projects/{project_name}"
    generation_message = generate_fastapi_project(project_name, analysis_result)

    generate_unit_tests(project_path,analysis_result)
    generate_code_from_tests(project_path)

    generate_readme(project_path,analysis_result)

    generate_api_docs(project_path,analysis_result)

    generate_mermaid_flow(project_path)

    zip_path=zip_project(project_path)

    summary_data={
        "project_name": project_name,
        "analysis": analysis_result,
        "zip_path": zip_path,
        "test_count": len(os.listdir(os.path.join(project_path,"tests"))),
        "service_count": len(os.listdir(os.path.join(project_path,"app","services"))),
        "status": "success"
    }

    save_result_summary(project_path,summary_data)


    return FileResponse(zip_path,filename=f"{project_name}.zip", media_type="application/zip")

    # return {
    #     "message": generation_message,
    #     "project_path": f"generated_projects/{project_name}",
    #     "zip_path":zip_path,
    #     "analysis": analysis_result
    # }
