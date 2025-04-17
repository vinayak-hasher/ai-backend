import os 
from app.langgraph_nodes.test_generator import call_groq

def generate_readme(project_path: str, analysis: dict):
    api_endpoints = analysis.get("api_endpoints",[])
    business_rules= analysis.get("business_rules",[])
    auth= analysis.get("auth_requirements",{})

    prompt= f"""
    Generate a professional README.md file for a FastAPI backend project.

    Project Requirements:
    - Functional API Endpoints: {api_endpoints}
    - Business Logic Rules: {business_rules}
    - Auth System: {auth}

    Include:
    - Project Title
    - Tech Stack
    - How to install and Run
    - Folder Structure
    - How to use the API
    - Auth info if available
    - Testing Instructions
    - No extra exlanation, just markdown content.
    """

    readme_content=call_groq(prompt)

    with open(os.path.join(project_path,"Readme.md"),"w") as f:
        f.write(readme_content)

def generate_api_docs(project_path: str, analysis:dict):
    endpoints= analysis.get("api_endpoints",[])
    content="# API Documentation\n\n"

    for ep in endpoints:
        method=ep.get("method","get")
        path=ep.get("path","/")
        desc= ep.get("description","No Description provided")
        params= ep.get("params",[])

        content +=f"### `{method.upper()} {path}`\n"
        content +=f"- **Description:** {desc}\n"
        if params:
            content+=f"- **Parameters:** {','.join(params)}\n"
        content+="\n---\n"

    with open(os.path.join(project_path,"api_docs.md"),"w") as f:
        f.write(content)
