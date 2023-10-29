@echo off
::This kills the Epic Games Overlay and therefore the Achievement Popup and Sound
set process_name=EOSOverlayRenderer-Win64-Shipping.exe

:loop
taskkill /f /im %process_name% >nul 2>&1
timeout /nobreak /t 1 >nul
goto loop
