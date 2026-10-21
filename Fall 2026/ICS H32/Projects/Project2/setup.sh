#!/bin/bash


PROJECT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") &> /dev/null && pwd -P)
SETUP_DIR=$PROJECT_DIR/.setup
VENV_DIR=.venv


cd $PROJECT_DIR


if [[ ! -e "$VENV_DIR" ]]; then
    echo "Creating a virtual environment ..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"

    echo "Installing all dependencies into the virtual environment ..."
    python3 "$SETUP_DIR/install_dependencies.py"

    if [[ ! -e "$PROJECT_DIR/src" ]]; then
        echo "Creating src/ directory ..."
        mkdir -p "$PROJECT_DIR/src"
    fi

    echo "Making all Python modules in the src/ directory visible everywhere ..."
    python3 "$SETUP_DIR/write_project_path.py"
fi
