import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'mlproject'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
] 

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating the file directory:{filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"creating empty file: {file_path}")

    else:
        logging.info(f"{filename} is already exists")        