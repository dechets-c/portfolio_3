@echo off
setlocal

set ROOT=%~dp0..
set BACKEND=%ROOT%\src\backend
set FRONTEND=%ROOT%\src\frontend

if not exist "%BACKEND%\.env" (
    echo [!] Fichier %BACKEND%\.env manquant.
    copy "%BACKEND%\.env.example" "%BACKEND%\.env" >nul
    echo Un .env vide a ete cree a partir de .env.example.
    echo Renseigne db_name, db_user, db_password, db_host et secret_key, puis relance ce script.
    pause
    exit /b 1
)

echo Lancement du backend FastAPI sur http://127.0.0.1:8000 ...
start "Backend - FastAPI" cmd /k "cd /d "%BACKEND%" && uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

if not exist "%FRONTEND%\node_modules" (
    echo Installation des dependances frontend (premiere fois)...
    pushd "%FRONTEND%"
    call npm install
    popd
)

echo Lancement du frontend React sur http://localhost:3000 ...
start "Frontend - React" cmd /k "cd /d "%FRONTEND%" && npm start"

echo.
echo Portfolio public : http://localhost:3000
echo Interface admin  : http://localhost:3000/#b7a9f3c2
endlocal
