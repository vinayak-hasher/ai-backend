import os
import shutil

PROJECT_BASE = "generated_projects"

def generate_fastapi_project(project_name: str,analysis:dict):
    base_path = os.path.join(PROJECT_BASE, project_name)

    if os.path.exists(base_path):
        shutil.rmtree(base_path)

    paths = [
        f"{base_path}/app/api/routes",
        f"{base_path}/app/models",
        f"{base_path}/app/services",
        f"{base_path}/tests"
    ]

    for path in paths:
        os.makedirs(path, exist_ok=True)

    write_file(f"{base_path}/app/main.py", main_py_content())
    write_file(f"{base_path}/app/database.py", database_py_content())
    write_file(f"{base_path}/requirements.txt", requirements_content())
    write_file(f"{base_path}/.env", env_content())
    write_file(f"{base_path}/Dockerfile", dockerfile_content())
    write_file(f"{base_path}/README.md", readme_content())

    write_routes(analysis.get("api_endpoints",[]),base_path)
    write_models(analysis.get("database_schema",[]),base_path)

    return f"Project '{project_name}' created at {base_path}"


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

def main_py_content():
    return '''from fastapi import FastAPI
from app.api.routes import example

app = FastAPI()
app.include_router(example.router)
'''

def database_py_content():
    return '''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
'''

def requirements_content():
    return '''fastapi
uvicorn
sqlalchemy
python-dotenv
psycopg2-binary
'''

def env_content():
    return '''DATABASE_URL=postgresql://username:password@localhost:5432/dbname
'''

def dockerfile_content():
    return '''FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''

def readme_content():
    return "# Auto-generated FastAPI project\n\nRun with:\n```bash\nuvicorn app.main:app --reload\n```"


def write_routes(endpoints, base_path):
    route_file = f"{base_path}/app/api/routes/example.py"
    content = "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n"
    for ep in endpoints:
        method = ep.get("method", "get").lower()
        path = ep.get("path", "/")
        func_name = path.strip("/").replace("/", "_") or "root"
        content += f"@router.{method}(\"{path}\")\ndef {func_name}():\n    return {{\"message\": \"{func_name} endpoint placeholder\"}}\n\n"
    write_file(route_file, content)

def write_models(schema, base_path):
    model_file = f"{base_path}/app/models/models.py"
    tables = schema.get("tables", {})

    print("Table detetecd", type(tables), tables)

    if isinstance(tables,list):
        tables={t["name"]:{"columns": t.get("columns",[])} for t in tables if "name" in t}

    content = "from sqlalchemy import Column, Integer, String\nfrom app.database import Base\n\n"

    for table_name, table_data in tables.items():
        class_name = table_name.capitalize()
        content += f"class {class_name}(Base):\n"
        content += f"    __tablename__ = '{table_name}'\n"
        for col in table_data.get("columns", []):
            content += f"    {col} = Column(String)\n"
        content += "\n"

    write_file(model_file, content)
