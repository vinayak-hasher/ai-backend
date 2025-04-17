from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.docx_parser import extract_text_from_docx
from app.langgraph_nodes.srs_analysis import analyze_srs_content
from app.langgraph_nodes.project_generator import generate_fastapi_project
from app.langgraph_nodes.test_generator import generate_unit_tests
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

    # STEP 1: Parse and analyze the SRS
    srs_text = extract_text_from_docx(file_path)
    # raw_result = analyze_srs_content(srs_text)

    # try:
    #     analysis_result = json.loads(raw_result)
    # except json.JSONDecodeError:
    #     return {"error": "Invalid JSON from Groq", "raw_output": raw_result}

    analysis_result=analyze_srs_content(srs_text)

    # STEP 2: Feed analysis into Milestone 2 generator
    project_name = file.filename.replace(".docx", "")
    generation_message = generate_fastapi_project(project_name, analysis_result)

    project_path=f"generated_projects/{project_name}"
    generate_unit_tests(project_path,analysis_result)

    return {
        "message": generation_message,
        "project_path": f"generated_projects/{project_name}",
        "analysis": analysis_result
    }
