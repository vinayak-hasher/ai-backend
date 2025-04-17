import subprocess
import os
from app.langgraph_nodes.test_generator import call_groq

MAX_RETRIES=0

def run_pytest(project_path: str) -> tuple[bool,str]:
    result=subprocess.run(
        ["pytest","--tb=short"],
        cwd= project_path,
        capture_output=True,
        text=True
    )
    success=result.returncode==0
    return success,result.stdout + "\n" + result.stderr

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

    Fix the code so all tests pass.

    Return only the updated,working code. No extra explanation.
    """

    return call_groq(prompt)