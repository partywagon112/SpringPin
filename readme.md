# Spring Pin
A few KiCad plugins meant to help with automating tasks required for spring pins.

The best way to automate assembly for PCBs where spring pins are used where connectors normally are is to add in individual items. 
This can be tedious, so some automation is necessary. 

# Installation (Kicad 6.0 >)
Run setup.bat for Windows, this shoud ROBOCOPY everything into position... if it fails, you have to tinker.

Linux assume you know what you're doing, cp ./src/SpringPin into the plugins directory.

# Future
Probably should make something that can interact with the schematic to place the required items... but too hard! 
C'mon KiCad provide a Python API for EESchema.
