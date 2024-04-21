import os
import shutil
import typer
from pathlib import Path

app = typer.Typer()

docs_path = Path("docs")
site_path = Path("site")

@app.command()
def build() -> None:
    shutil.rmtree(docs_path, ignore_errors=True)
    os.rename(site_path, docs_path)

if __name__ == "__main__":
    app()