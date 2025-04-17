import json 
import os

def save_result_summary(project_path:str, summary_data:dict):
    file_path=os.path.join(project_path,"result_summary.json")
    with open(file_path,"w") as f:
        json.dump(summary_data,f,indent=2)