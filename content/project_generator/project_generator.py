import os
import zipfile
import tempfile
from pathlib import Path
import argparse
import shutil
import sys

def create_project_structure(project_name):
    # Create a temporary directory for the project
    base_dir = Path(tempfile.mkdtemp()) / project_name
    base_dir.mkdir(parents=True, exist_ok=True)

    # Create directories
    (base_dir / "src" / project_name).mkdir(parents=True, exist_ok=True)
    (base_dir / "tests").mkdir(parents=True, exist_ok=True)

    # Add __init__.py and main.py
    (base_dir / "src" / project_name / "__init__.py").touch()
    with open(base_dir / "src" / project_name / "main.py", "w") as f:
        f.write("# Main script goes here\n")

    # Add test file
    with open(base_dir / "tests" / "test_main.py", "w") as f:
        f.write("# Unit tests go here\n")

    # Copy pyproject.toml, gitignore, tasks.py, and README.md files from the local directory
    required_files = ["pyproject.toml", "gitignore.txt", "tasks.py", "README.md"]  # List includes README.md
    for file_name in required_files:
        file_path = Path(file_name)
        if not file_path.exists():
            print(f"Error: Required file '{file_name}' not found in the current directory.")
            sys.exit(1)  # Exit the script with an error code if a file is missing
        destination_file = base_dir / (".gitignore" if file_name == "gitignore.txt" else file_name)
        shutil.copy(file_path, destination_file)

    return base_dir

def package_project(base_dir, output_file):
    # Create a zip file of the project
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(base_dir.parent))
    print(f"Project packaged into {output_file}")

def main(project_name=None, output_file="project.zip"):
    if project_name is None:
        # Use argparse to handle arguments if none are passed
        parser = argparse.ArgumentParser(description="Generate a Python project structure.")
        parser.add_argument("project_name", help="The name of the project")
        parser.add_argument("--output", default="project.zip", help="The output zip file")
        args = parser.parse_args()
        project_name = args.project_name
        output_file = args.output

    # Create project structure
    base_dir = create_project_structure(project_name)
    
    try:
        # Package the project into a zip file
        package_project(base_dir, output_file)
    finally:
        # Clean up the temporary directory
        shutil.rmtree(base_dir)

if __name__ == "__main__":
    main()
