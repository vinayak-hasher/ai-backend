import os
import httpx
import time
from dotenv import load_dotenv
load_dotenv()

API_KEYS=[os.getenv("GROQ_API_KEY"),os.getenv("GROQ_API_KEY_2")]
MODEL_NAME= "llama3-70b-8192"

def call_groq(prompt:str, max_retries=3):
    url="https://api.groq.com/openai/v1/chat/completions"
    body={
        "model": MODEL_NAME,
        "messages":[
            {
                "role":"system",
                "content": "You are a senior Pyhton backend Developer who writes clean,tested code."
            },
            {
                "role":"user",
                "content": prompt
            }
        ],
        "temperature":0.2
    }

    for key in API_KEYS:
        for attempt in range(max_retries):
            try:
                headers={"Authorization":f"Bearer {key}","Content-Type": "application/json"}
                response= httpx.post(url,headers=headers,json=body)
                response.raise_for_status()
                output= response.json()["choices"][0]["message"]["content"]
                time.sleep(2)
                return output
            
            except httpx.HTTPStatusError as e:
                if e.response.status_code==429:
                    wait=2**attempt
                    print("Waiting")
                    time.sleep(wait)
                else :
                    raise e
        print("Key Switching")
    raise Exception("All Keys gone")

def generate_unit_tests(project_path: str, analysis: dict):
    services=analysis.get("business_rules",[])
    test_folder=os.path.join(project_path,"tests")
    os.makedirs(test_folder,exist_ok=True)

    for idx, rule in enumerate(services):
        prompt= f"""
        Based on the following business rule, generate a pytest-style unit test with proper assertions and edge cases.filter

        Rule: {rule}

        Return only code - do not explain.
        """

        test_code=call_groq(prompt)
        file_path=os.path.join(test_folder, f"test_service_{idx+1}.py")
        with open(file_path, "w") as f:
            f.write(test_code)

