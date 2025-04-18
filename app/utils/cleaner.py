import re

def clean_code_block(code: str)->str:

    pattern= r"```(?:python)?\n([\s\S]+?)\n```"
    match= re.search(pattern,code.strip())

    if match:
        return match.group(1).strip()
    
    lines=code.strip().splitlines()

    for i, line in enumerate(lines):    
        if line.strip().startswith("```"):
            return "\n".join(lines[i+1:-1])
    return code