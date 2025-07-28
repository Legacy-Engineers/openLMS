#!/usr/bin/env python3
"""
Script to fix import statements by adding 'apps.' prefix where needed
"""

import os
import re
from pathlib import Path

# Apps that need the 'apps.' prefix
APPS = [
    "accounts",
    "customers",
    "services",
    "orders",
    "expenses",
    "reports",
    "system_settings",
    "loyalty",
]


def fix_imports_in_file(file_path):
    """Fix imports in a single file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Fix from imports
        for app in APPS:
            # Pattern: from app_name. (but not from apps.app_name.)
            pattern = rf"from {app}\."
            replacement = f"from apps.{app}."
            content = re.sub(pattern, replacement, content)

        # Fix import statements
        for app in APPS:
            # Pattern: import app_name (but not import apps.app_name)
            pattern = rf"import {app}(?!\.)"
            replacement = f"import apps.{app}"
            content = re.sub(pattern, replacement, content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed imports in: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to fix all imports"""
    project_root = Path(".")
    fixed_count = 0

    # Find all Python files
    for py_file in project_root.rglob("*.py"):
        # Skip the fix_imports.py script itself
        if py_file.name == "fix_imports.py":
            continue

        # Skip files in .venv or other virtual environments
        if ".venv" in str(py_file) or "venv" in str(py_file):
            continue

        if fix_imports_in_file(py_file):
            fixed_count += 1

    print(f"\nFixed imports in {fixed_count} files")


if __name__ == "__main__":
    main()
