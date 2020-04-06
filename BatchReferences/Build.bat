@echo off

call Update_From_P4.bat
rem call Build_Lighting.bat
call Build_Game.bat
call Build_Installer.bat
call Update_Deleted_Nightly.bat