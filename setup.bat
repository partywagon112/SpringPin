@echo off

set mypath=%cd%
call "C:\Program Files\KiCad\7.0\bin\kicad-cmd.bat"
cd %mypath%
call pip install --editable .

if exist "C:\Users\%username%\OneDrive\Documents\KiCad\7.0\scripting\plugins" (
    robocopy .\src\ C:\Users\%username%\OneDrive\Documents\KiCad\7.0\scripting\plugins /E
) else (
    if exist "C:\Users\%username%\Documents\KiCad\7.0\scripting\plugins" (
        robocopy .\src\ C:\Users\%username%\Documents\KiCad\7.0\scripting\plugins /E
    ) else (
        echo No directory found to install plugins! Copy and Paste ./src/SpringPin manually into the KiCad plugins directory.
    )
)

echo Done
pause
