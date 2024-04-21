import os
import json
import shutil
import subprocess
from pathlib import Path
from typing import List

default_lang = "zh"
docs_path = Path("docs")
site_path = Path("site").absolute()

def get_available_lang_paths() -> List[Path]:
    return sorted(docs_path.iterdir())


def langs_json():
    langs = []
    for lang_path in get_available_lang_paths():
        if lang_path.is_dir():
            langs.append(lang_path.name)
    print(json.dumps(langs))

def build_lang(lang_code: str) -> None:
    lang_path = Path("docs") / lang_code
    if lang_code == default_lang:
        dist_path = site_path
    else:
        dist_path = site_path / lang_code
        shutil.rmtree(dist_path, ignore_errors=True)
    current_dir = os.getcwd()
    os.chdir(lang_path)
    subprocess.run(["mkdocs", "build", "--site-dir", dist_path], check=True)
    os.chdir(current_dir)