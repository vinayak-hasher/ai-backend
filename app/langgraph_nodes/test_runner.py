import subprocess
import os
import re
from app.langgraph_nodes.test_generator import call_groq
from app.langgraph_nodes.langsmith_logger import log_fix_attempt

MAX_RETRIES=2


def run_pytest(project_path: str) -> tuple[bool,str]:
    result=subprocess.run(
        ["pytest","--tb=short"],
        cwd= project_path,
        capture_output=True,
        text=True
    )
    output=result.stdout+"\n"+ result.stderr
    success=result.returncode==0

    logs_dir=os.path.join(project_path,"logs")
    os.makedirs(logs_dir,exist_ok=True)

    with open(os.path.join(logs_dir,"pytest.log"),"a") as f:
        f.write(f"\n=== Pytest Run ===\n{output}")

    return success,output

def fix_code_with_groq(test_code: str, error:str, broken_code: str)-> str:
    prompt= f"""
    You are a senior Python Backend Developer.
    The following unit test failed:
    ===TEST===
    {test_code}

    ===Error Output===
    {error}

    ===Current Code===
    {broken_code}

    Please:
    - Fix only the broken logic
    - Preserve inputs, function names, and structures
    - Focus on fixing the AssertionError
    - Return only corrected Python code with no explanation.

    """

    return call_groq(prompt)