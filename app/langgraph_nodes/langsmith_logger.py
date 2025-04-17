from langsmith import traceable
from langsmith.client import Client
import os

client=Client()

@traceable(name="analyze_srs_with_groq")
def log_srs_analysis(input_text: str, response: dict):
    return response

@traceable(name="generate_tests_with_groq")
def log_test_generation(rule:str, test_code:str):
    return test_code

@traceable(name="generate_code with_groq")
def log_code_generation(test_name:str, test_code:str, result_code: str):
    return result_code

@traceable(name="fix_code_attempt")
def log_fix_attempt(attempt:int, error:str, fixed_code=str):
    return fixed_code

