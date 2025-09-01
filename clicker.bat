@echo off
REM Change into refactoredCode, relative to this batch file
cd /d "%~dp0refactoredCode"

REM Check if Python is installed
python --version >nul 2>&1
if ERRORLEVEL 1 (
    echo Python is not installed!
    echo Please download and install Python from provided python file
    pause
    exit /b
)

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo ERROR: requirements.txt not found in %cd%
    pause
    exit /b
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if main.py exists
if not exist main.py (
    echo ERROR: main.py not found in %cd%
    pause
    exit /b
)

REM Run the game
echo Starting the game!
python main.py
