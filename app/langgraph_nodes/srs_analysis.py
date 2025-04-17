import os
import httpx
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("GROQ_API_KEY")
# print("GROQ: ", os.getenv("GROQ_API_KEY"))
MODEL_NAME="llama3-70b-8192"

def get_groq_response(prompt: str)->str:
    url="https://api.groq.com/openai/v1/chat/completions"
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body={
        "model": MODEL_NAME,
        "messages":[
            {
                "role":"system",
                "content": "You are an expert software architect. Your job is to extract structured data in JSON Format."

            },
            {
                "role":"user",
                "content": prompt
            }
        ],
        "temperature":0.2
    }

    response = httpx.post(url,headers=headers,json=body)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

def analyze_srs_content(text: str)->dict:
    prompt= f"""
    Analyze the following Software Requirements Specification and returned structured JSON with:

    - api_endpoints: list of endpoints with method, path, description
    - database_schema: tables,columns,relationships
    - business_rules: textual rules and logic to be enforced
    - auth_requirements: roles,login mechanisms, etc.

    Return Only JSON. Do not add any explanation or markdown,or explanation. Make sure JSON is parsable using json.loads().

    SRS:
    {text}
    """

    raw_response= get_groq_response(prompt)

    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        import re
        json_text = re.search(r'\{.*\}', raw_response,re.DOTALL)
        if json_text:
            return json.loads(json_text.group())
        else:
            return{"error": "Failed to parse JSON from model response","raw":raw_response}
