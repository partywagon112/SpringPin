@echo off

set mypath=%cd%
call "C:\Program Files\KiCad\7.0\bin\kicad-cmd.bat"
cd %mypath%
call pip install -r requirements.txt

if exist "C:\Users\%username%\OneDrive\Documents\KiCad\7.0\scripting\plugins" (
    robocopy .\src\SpringPin C:\Users\%username%\OneDrive\Documents\KiCad\7.0\scripting\plugins\SpringPin /E
) else (
    if exist "C:\Users\%username%\Documents\KiCad\7.0\scripting\plugins" (
        robocopy .\src\SpringPin C:\Users\%username%\Documents\KiCad\7.0\scripting\plugins\SpringPin /E
    ) else (
        echo No directory found to install plugins! Copy and Paste ./src/SpringPin manually into the KiCad plugins directory.
    )
)

echo Done
pause
