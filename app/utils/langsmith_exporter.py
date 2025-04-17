import json
import os
from app.langgraph_nodes.langsmith_logger import executed_traces

def save_langsmith_trace(project_path: str):
    trace_data={
        "langsmith_project": os.getenv("LANGCHAIN_PROJECT"),
        "trace_run_ids": executed_traces,
        "dashboard_link": f"https://smith.langchain.com/projects/{os.getenv('LANGCHAIN_PROJECT')}"
    }

    with open(os.path.join(project_path,"langsmith_trace.json"),"w") as f:
        json.dump(trace_data,f,indent=2)
