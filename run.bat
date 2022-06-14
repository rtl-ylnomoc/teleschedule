@REM This batch script activates venv and starts the bot with start.py entry point.

@echo off

call %~dp0env\Scripts\activate

python start.py

pause
