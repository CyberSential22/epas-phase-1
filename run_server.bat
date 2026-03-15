@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo   Event Planner ^& Approval System - FIRST TIME SETUP
echo ========================================================

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: 2. Create Virtual Environment
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
) else (
    echo [INFO] Virtual environment already exists.
)

:: 3. Activate Virtual Environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate

:: 4. Upgrade pip and install requirements
echo [INFO] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

:: 5. Initialize .env file if it doesn't exist
if not exist ".env" (
    echo [INFO] Creating .env file...
    for /f "tokens=*" %%a in ('python -c "import secrets; print(secrets.token_hex(32))"') do set SECRET=%%a
    echo SECRET_KEY=!SECRET!> .env
    echo FLASK_APP=run.py>> .env
    echo FLASK_CONFIG=development>> .env
    echo FLASK_DEBUG=1>> .env
    echo [SUCCESS] .env file created with secure SECRET_KEY.
)

:: 6. Initialize Database (optional, handled by run.py)
echo [INFO] Initializing system database...

:: 7. Start Server
echo [SUCCESS] Setup complete! Starting the server...
python run.py

pause
