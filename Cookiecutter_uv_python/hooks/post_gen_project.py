#!/usr/bin/env python3
"""Post-generation hook to clean up generated project."""

import os
import shutil
from pathlib import Path


def remove_pycache(directory: Path) -> None:
    """Recursively remove all __pycache__ directories."""
    for item in directory.rglob("*"):
        if item.is_dir() and item.name == "__pycache__":
            shutil.rmtree(item)
            print(f"Removed: {item}")


if __name__ == "__main__":
    project_path = Path("{{ cookiecutter.project_slug }}")
    if project_path.exists():
        remove_pycache(project_path)
