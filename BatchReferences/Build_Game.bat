@echo off

rem Here it could be useful to echo the build log to a text file so you can see the error if the build fails.
echo ----------------------------------------------------------------------
echo Step 2: Packaging unreal project into archive
echo ----------------------------------------------------------------------

set base_dir=C:\AutomatedBuilds\C28\TGP3\Tex_Mechs\
set project_dir=%base_dir%Project_Files\TexMechs\
set uproject_file="%project_dir%TexMechs.uproject"
set builds_dir=%base_dir%Build_Dir_C29_Test\
set build_maps="/Game/Levels/UI_MainMenu+/Game/Levels/MechBay+/Game/Levels/PLVL_Canyon_Alpha"

call "C:\Program Files\Epic Games\UE_4.22\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -clientconfig=Shipping -serverconfig=Shipping -nocompile -nocompileeditor -installed -ue4exe=UE4Editor-Cmd.exe -utf8output -platform=Win64 -build -cook -map=%build_maps% -unversionedcookedcontent -encryptinifiles -pak -createreleaseversion= -SkipCookingEditorContent -compressed -prereqs -stage -package -stagingdirectory=%builds_dir% -archive -archivedirectory=%builds_dir%
rem call "C:\Program Files\Epic Games\UE_4.22\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -platform=Win64 -clientconfig=Shipping -serverconfig=Shipping -cook -maps=%build_maps% -build -stage -pak -archive -archivedirectory=%builds_dir%
echo:
echo:

pause


rem Here I do a check to ensure the build was successful
rem With these programs, they return 0 on success, so if non-zero return code, just go to fail case below and DON'T make an installer
rem Otherwise it will create an installer with the last working build.
IF %ERRORLEVEL% NEQ 0 ( 
    echo ----------BUILD FAILED - HALTING BATCH PROCESS----------
	echo PUSHING A TXT FILE TO DELETED NIGHTLY TO SIGNAL BAD BUILD
	net use F: "%network_dir%" gKv52w!* /USER:smu\dummy /PERSISTENT:NO
	echo. 2>%network_dir%/BUILD_BROKEN.txt
	net use F: /d
	echo. 2>%builds_dir%/BUILD_BROKEN.txt
	exit 1
)

rem Adding the steam file to the made build and writing our steam app ID
rem SteamAppID > PathToCreateTextFileAt
rem echo ----------------------------------------------------------------------
rem echo Step 2.5: Adding steam file to build
rem echo ----------------------------------------------------------------------
rem echo 934840 > C:\AutomatedBuilds\C27\Capstone\ThinkArcade\Build_Dir\WindowsNoEditor\FrostRunner\Binaries\Win64\steam_appid.txt