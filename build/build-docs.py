import os
import shutil
import typer
from pathlib import Path

app = typer.Typer()

docs_path = Path("docs")
site_path = Path("site")
artifact = Path("artifacts")

@app.command()
def build() -> None:
    shutil.rmtree(docs_path, ignore_errors=True)
    shutil.move(artifact / site_path, Path("/"))
    os.rename(site_path, docs_path)
    shutil.rmtree(artifact)

if __name__ == "__main__":
    app()