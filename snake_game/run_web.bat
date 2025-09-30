@echo off
title ByteSnake Web Version
color 0A

echo.
echo  🐍 ByteSnake Web Version Launcher 🐍
echo  ====================================
echo.
echo  Starting web server...
echo  Opening game in browser...
echo  Server: http://localhost:8000
echo.
echo  Press Ctrl+C to stop the server
echo.

start http://localhost:8000
python -m http.server 8000
