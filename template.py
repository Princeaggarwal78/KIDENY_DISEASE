import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s:')

project_name  = 'CNN'


files = [
        ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


for file_path in files:

    file_path = Path(file_path)
    file_direct , file_name = os.path.split(file_path)
    
    if file_direct != '':
        os.makedirs(file_direct,exist_ok=True)
        logging.info(f"creating directory {file_direct} for the file: {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
        logging.info(f"creating empty file {file_name}")

    else :
        logging.info(f"{file_name} is already exist")