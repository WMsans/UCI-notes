@echo off


set PROJECT_DIR=%~dp0
set SETUP_DIR=%PROJECT_DIR%\.setup
set VENV_DIR=.venv


cd %PROJECT_DIR%


if not exist "%VENV_DIR%\" (
    echo Creating a virtual environment ...
    python -m venv %VENV_DIR%
    %VENV_DIR%\Scripts\activate.bat

    echo Installing all dependencies into the virtual environment ...
    python "%SETUP_DIR%\install_dependencies.py"

    if not exist "%PROJECT_DIR%\src" (
        echo Creating src/ directory ...
        mkdir "%PROJECT_DIR%\src"
    )

    echo Making all Python modules in the src/ directory visible everywhere ...
    python "%SETUP_DIR%\write_project_path.py"
)
