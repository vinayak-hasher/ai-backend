from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.docx_parser import extract_text_from_docx
from app.langgraph_nodes.srs_analysis import analyze_srs_content
import os

router=APIRouter()

@router.post("/analyze-srs")
async def analyze_srs(file: UploadFile =File(...)):
    if not file.filename.endswith(".docx"):
        raise HTTPException(status_code=400,detail="Only .docx files are supported.")
    
    os.makedirs("temp",exist_ok=True)
    file_path=f"temp/{file.filename}"
    with open(file_path,"wb") as f:
        f.write(await file.read())

    srs_text=extract_text_from_docx(file_path)
    result= analyze_srs_content(srs_text)

    return{"result" : result}