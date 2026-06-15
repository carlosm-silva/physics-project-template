"""Post-generation hooks — remove optional directories based on user choices."""

import shutil
from pathlib import Path

PROJECT_DIR = Path.cwd()

if "{{cookiecutter.has_paper}}" != "y":
    shutil.rmtree(PROJECT_DIR / "paper", ignore_errors=True)
