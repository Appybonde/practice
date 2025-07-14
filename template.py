import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "ml-project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/data_ingestion/__init__.py",
    f"src/{project_name}/data_transformation/__init__.py",
    f"src/{project_name}/model_trainer/__init__.py",
    f"src/{project_name}/model_monitoring/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    "app.py",
    "logger.py",
    "requirements.txt",
    "setup.py"
]


for file_path in list_of_files:
    file_dir = os.path.dirname(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Created file: {file_path}")
    else:
        logging.warning(f"File already exists: {file_path}")
