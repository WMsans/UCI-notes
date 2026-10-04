from pathlib import Path
import subprocess
import sys
import tomllib


# Installs all dependencies listed in 'pyproject.toml' if (and only if) that file exists in the
# project's root directory.


def run() -> None:
    project_path = Path.cwd()
    pyproject_toml_path = project_path / 'pyproject.toml'

    if pyproject_toml_path.is_file():
        with pyproject_toml_path.open('rb') as pyproject_file:
            pyproject_data = tomllib.load(pyproject_file)

        if 'project' in pyproject_data and 'dependencies' in pyproject_data['project']:
            dependencies = pyproject_data['project']['dependencies']
            subprocess.run([sys.executable, '-m', 'pip', 'install', *dependencies])


if __name__ == '__main__':
    run()
