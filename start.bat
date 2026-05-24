@echo off
REM Waste Sense - one-click launcher (Windows)
REM Place best.pt in this folder before running.

if not exist best.pt (
    echo [ERROR] best.pt not found in this folder.
    echo Download it from your Google Drive and place it here.
    pause
    exit /b 1
)

echo Installing dependencies (first run only)...
pip install -r requirements.txt

echo Starting backend at http://localhost:8000 ...
start "" index.html
uvicorn server:app --host 0.0.0.0 --port 8000
