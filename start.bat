@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 goto try_python
py -3 -c "import sys, tkinter; assert sys.version_info.major == 3" >nul 2>nul
if errorlevel 1 goto try_python
py -3 app.py
if errorlevel 1 goto app_error
exit /b 0

:try_python
where python >nul 2>nul
if errorlevel 1 goto missing_python
python -c "import sys, tkinter; assert sys.version_info.major == 3" >nul 2>nul
if errorlevel 1 goto missing_python
python app.py
if errorlevel 1 goto app_error
exit /b 0

:missing_python
echo Python 3 with tkinter was not found.
echo Install Python 3 for Windows with Tcl/Tk support and Python Launcher.
echo Then run start.bat again.
pause
exit /b 1

:app_error
echo The application could not start. Read the error above.
pause
exit /b 1
