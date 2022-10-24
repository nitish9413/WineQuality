import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

package_name = 'wineQuality'

list_of_files= [
    ".github/workflows/.gitkeep",
    f"{package_name}/components/__init__.py",
    f"{package_name}/utils/__init__.py",
    f"{package_name}/config/__init__.py",
    f"{package_name}/constant/__init__.py",
    f"{package_name}/entity/__init__.py",
    f"{package_name}/exception/__init__.py",
    f"{package_name}/logger/__init__.py",
    f"{package_name}/pipeline/__init__.py",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
    "configs/config.yaml",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")
    if (not filepath.exists()) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"File {filename} already exists")