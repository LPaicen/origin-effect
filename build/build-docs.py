import os
import shutil
from pathlib import Path

docs_path = Path("docs")
site_path = Path("site")

def build() -> None:
    shutil.rmtree(docs_path, ignore_errors=True)
    os.rename(site_path, docs_path)