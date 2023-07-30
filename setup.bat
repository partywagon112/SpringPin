@echo off

set mypath=%cd%
call "C:\Program Files\KiCad\7.0\bin\kicad-cmd.bat"
cd %mypath%
call pip install --editable .

@REM robocopy .\src\ C:\Users\%username%\OneDrive\Documents\KiCad\7.0\scripting\plugins /E
robocopy .\src\ %APPDATA%/Roaming/kicad/scripting/plugins /E

echo Done
pause