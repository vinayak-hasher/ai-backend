import os
from app.langgraph_nodes.test_generator import call_groq

def generate_code_from_tests(project_path: str):
    test_folder= os.path.join(project_path,"tests")
    service_folder=os.path.join(project_path,"app","services")
    os.makedirs(service_folder,exist_ok=True)

    for filename in os.listdir(test_folder):
        if not filename.startswith("test_") or not filename.endswith(".py"):
            continue

        file_path=os.path.join(test_folder,filename)

        with open(file_path,"r") as f:
            test_code=f.read()

        prompt=f"""
        The following is a pytest test case file.
        Your task is to write a FastAPI-compatible Pyhton service function that will pass all these tests.
        Follow good coding practices, handle edge cases, and return only the code.

        Test File Content:
        {test_code}
        """

        impl_code=call_groq(prompt)

        service_filename=filename.replace("test_","").replace(".py","_service.py")
        service_path= os.path.join(service_folder, service_filename)
        with open(service_path, "w") as f:
            f.write(impl_code)