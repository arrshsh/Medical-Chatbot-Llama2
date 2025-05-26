import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: %(levelname)s: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

for path in list_of_files:
    filepath = Path(path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 if os.path.isfile(filepath) else False):
        if not os.path.isdir(filepath):  # Only create file if it's not a directory
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"{filepath} already exists")