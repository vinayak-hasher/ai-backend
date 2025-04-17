import os
from app.langgraph_nodes.test_generator import call_groq
from app.langgraph_nodes.test_runner import run_pytest, fix_code_with_groq,MAX_RETRIES
import time

def generate_code_from_tests(project_path: str):
    test_folder= os.path.join(project_path,"tests")
    service_folder=os.path.join(project_path,"app","services")
    os.makedirs(service_folder,exist_ok=True)

    for idx,filename in enumerate(test_folder):
        if idx>=1:
            break
        if not filename.startswith("test_") or not filename.endswith(".py"):
            continue
        

        test_path=os.path.join(test_folder,filename)
        service_filename=filename.replace("test_","").replace(".py","_service.py")
        service_path= os.path.join(service_folder, service_filename)

        with open(test_path,"r") as f:
            test_code=f.read()

        prompt=f"""
        You are a backend developer.
        This is a pytest unit test.
        ===
        {test_code}
        ===
        Write a FASTAPI-compatible service implementation that will pass this test.

        Enusre:
        - All edge cases are covered
        - Return types and value match expectations
        - Use correct imports and exception handling.
        - Return only Python code. No Explanation.

        This code should be placed in 'app/services/ and should work standalone.
        """

        code=call_groq(prompt)

        for attempt in range(MAX_RETRIES+1):
            with open(service_path, "w") as f:
                f.write(code)

            success, output = run_pytest(project_path)
            if success:
                print(f"Tests passed on attempt {attempt+1}")
                break

            print(f"Test failed on attempt {attempt+1}")
            code= fix_code_with_groq(test_code,output,code)