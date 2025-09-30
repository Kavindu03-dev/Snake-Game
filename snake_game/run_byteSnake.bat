@echo off
title ByteSnake Launcher
color 0A

echo.
echo  ===============================================
echo  🐍 ByteSnake - Enhanced Snake Game Launcher 🐍
echo  ===============================================
echo.

:menu
echo  Choose how to run ByteSnake:
echo.
echo  [1] Web Version (Recommended - No installation required)
echo  [2] Python Version (Requires pygame)
echo  [3] Install Python Dependencies
echo  [4] Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto web
if "%choice%"=="2" goto python
if "%choice%"=="3" goto install
if "%choice%"=="4" goto exit
echo Invalid choice. Please try again.
goto menu

:web
echo.
echo  🌐 Starting ByteSnake Web Version...
echo  Opening in your default browser...
echo  Server will run on: http://localhost:8000
echo  Press Ctrl+C to stop the server
echo.
start http://localhost:8000
python -m http.server 8000
goto menu

:python
echo.
echo  🐍 Starting ByteSnake Python Version...
echo  Checking for pygame...
python -c "import pygame" 2>nul
if %errorlevel% neq 0 (
    echo  ❌ pygame not found! Please install dependencies first.
    echo  Run option 3 to install dependencies.
    pause
    goto menu
)
echo  ✅ pygame found! Starting game...
cd /d "%~dp0"
python main.py
goto menu

:install
echo.
echo  📦 Installing Python Dependencies...
echo  Installing pygame...
pip install -r requirements.txt
if %errorlevel% equ 0 (
    echo  ✅ Dependencies installed successfully!
) else (
    echo  ❌ Installation failed. Please check your Python installation.
)
pause
goto menu

:exit
echo.
echo  👋 Thanks for playing ByteSnake!
echo  Game created with ❤️
pause
exit
