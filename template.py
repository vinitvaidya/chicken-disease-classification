import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"


#Create the list of files to be created in the project
list_of_files = [

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

for filepath in list_of_files:
    filepath = Path(filepath) #to get Windows compatible path
    filedir, filename = os.path.split(filepath) # to get the directory and filename separately

    """to check if the directory is not empty,
    if it is not empty then we will create the directory"""
    if filedir != "": 
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    """to check if the file already exists or not,
     if it exists then we will not create it again, if it does not exist then we will create it"""
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

    