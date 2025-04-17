import shutil
import os

def zip_project(project_path: str) ->str:
    zip_output_path=f"{project_path}.zip"

    if os.path.exists(zip_output_path):
        os.remove(zip_output_path)

    shutil.make_archive(project_path,'zip',project_path)
    return zip_output_path
