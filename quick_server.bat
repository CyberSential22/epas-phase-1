@echo off
echo ========================================================
echo   Event Planner & Approval System - QUICK START
echo ========================================================

:: Check for virtual environment
if not exist "venv" (
    echo [ERROR] Virtual environment not found. 
    echo Please run run_server.bat first to initialize the project.
    pause
    exit /b 1
)

:: Activate Virtual Environment
echo [INFO] Activating environment...
call venv\Scripts\activate

:: Check for .env file
if not exist ".env" (
    echo [WARNING] .env file missing. Server may not operate correctly.
)

:: Start Server
echo [INFO] Resuming Event Planner System...
python run.py

pause
