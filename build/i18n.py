import os
import json
import shutil
import subprocess
import typer
from pathlib import Path
from typing import List

app = typer.Typer()

default_lang = "zh"
docs_path = Path("docs")
site_path = Path("site").absolute()
build_site_path = Path("site_build").absolute()

def get_available_lang_paths() -> List[Path]:
    return sorted(docs_path.iterdir())

@app.command()
def langs_json():
    langs = []
    for lang_path in get_available_lang_paths():
        if lang_path.is_dir():
            langs.append(lang_path.name)
    print(json.dumps(langs))

@app.command()
def build_lang(lang_code: str) -> None:
    lang_path = Path("docs") / lang_code
    if not lang_path.is_dir():
        typer.echo(f"The language translation doesn't seem to exist yet: {lang_code}")
        raise typer.Abort()
    typer.echo(f"Building docs for: {lang_code}")
    build_site_dist_path = build_site_path / lang_code
    if lang_code == default_lang:
        dist_path = site_path
    else:
        dist_path = site_path / lang_code
        shutil.rmtree(dist_path, ignore_errors=True)
    current_dir = os.getcwd()
    os.chdir(lang_path)
    shutil.rmtree(build_site_dist_path, ignore_errors=True)
    subprocess.run(["mkdocs", "build", "--site-dir", build_site_dist_path], check=True)
    shutil.copytree(build_site_dist_path, dist_path, dirs_exist_ok=True)
    os.chdir(current_dir)
    typer.secho(f"Successfully built docs for: {lang_code}", color=typer.colors.GREEN)

if __name__ == "__main__":
    app()