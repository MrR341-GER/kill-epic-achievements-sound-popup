@echo off
::This kills the Epic Games Overlay and therefore the Achievement Popup and Sound
set process_name=EOSOverlayRenderer-Win64-Shipping.exe

:loop
tasklist | findstr /i %process_name% >nul
if not errorlevel 1 (
    taskkill /f /im %process_name%
    if errorlevel 1 (
        echo Failed to terminate the process.
    ) else (
        echo Process terminated.
    )
)
timeout /nobreak /t 1 >nul
goto loop