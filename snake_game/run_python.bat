@echo off
title ByteSnake Python Version
color 0A

echo.
echo  🐍 ByteSnake Python Version Launcher 🐍
echo  =======================================
echo.

REM Check if pygame is installed
python -c "import pygame" 2>nul
if %errorlevel% neq 0 (
    echo  ❌ pygame not found!
    echo  Installing dependencies...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo  ❌ Failed to install pygame. Please install manually:
        echo  pip install pygame
        pause
        exit
    )
    echo  ✅ Dependencies installed!
    echo.
)

echo  ✅ Starting ByteSnake...
echo  Use Arrow Keys or WASD to move
echo  Press P to pause/resume
echo  Press R to restart when game over
echo.

python main.py
