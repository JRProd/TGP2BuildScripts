import Environment

# Build the Game
# *Original from TexMech - C28 

# Here it could be useful to echo the build log to a text file so you can see the error if the build fails.
print( '----------------------------------------------------------------------' )
print( 'Step 2: Packaging unreal project into archive ')
print( '----------------------------------------------------------------------' )

section = "BuildGame"

base_dir = Environment.GetEnvVariable( section, "base_dir" )
project_dir = Environment.GetEnvVariable( section, "project_dir" )
uproject_file = Environment.GetEnvVariable( section, "uproject_file" )
builds_dir = Environment.GetEnvVariable( section, "builds_dir" )
build_maps = Environment.GetEnvVariable( section, "build_maps" )

print( base_dir )
print( project_dir )
print( uproject_file )
print( builds_dir )
print( build_maps )


#call "C:\Program Files\Epic Games\UE_4.23\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -nocompile -nocompileeditor -installed -cook -stage -archive -archivedirectory=%builds_dir% -package -clientconfig=Development -ue4exe="C:\Program Files\Epic Games\UE_4.23\Engine\Binaries\Win64\UE4Editor-Cmd.exe" -pak -prereqs -nodebuginfo -targetplatform=Win64 -build -CrashReporter -utf8output
# call "C:\Program Files\Epic Games\UE_4.23\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -clientconfig=Development -serverconfig=Development -ue4exe=UE4Editor-Cmd.exe -utf8output -installed -platform=Win64 -build -cook -map=%build_maps% -unversionedcookedcontent -pak -SkipCookingEditorContent -compressed -prereqs -stage -package -stagingdirectory=%builds_dir% -archive -archivedirectory=%builds_dir%
# call "C:\Program Files\Epic Games\UE_4.23\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -clientconfig=Shipping -serverconfig=Shipping -nocompile -nocompileeditor -installed -ue4exe=UE4Editor-Cmd.exe -utf8output -platform=Win64 -build -cook -map=%build_maps% -unversionedcookedcontent -encryptinifiles -pak -createreleaseversion= -SkipCookingEditorContent -compressed -prereqs -stage -package -stagingdirectory=%builds_dir% -archive -archivedirectory=%builds_dir%
# call "C:\Program Files\Epic Games\UE_4.22\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project=%uproject_file% -noP4 -platform=Win64 -clientconfig=Shipping -serverconfig=Shipping -cook -maps=%build_maps% -build -stage -pak -archive -archivedirectory=%builds_dir%


# Here I do a check to ensure the build was successful
# With these programs, they return 0 on success, so if non-zero return code, just go to fail case below and DON'T make an installer
# Otherwise it will create an installer with the last working build.
# IF %ERRORLEVEL% NEQ 0 ( 
#     echo ----------BUILD FAILED - HALTING BATCH PROCESS----------
# 	echo PUSHING A TXT FILE TO DELETED NIGHTLY TO SIGNAL BAD BUILD
# 	net use F: "%network_dir%" gKv52w!* /USER:smu\dummy /PERSISTENT:NO
# 	echo. 2>%network_dir%/BUILD_BROKEN.txt
# 	net use F: /d
# 	echo. 2>%builds_dir%/BUILD_BROKEN.txt
# )



# Adding the steam file to the made build and writing our steam app ID
# SteamAppID > PathToCreateTextFileAt
# echo ----------------------------------------------------------------------
# echo Step 2.5: Adding steam file to build
# echo ----------------------------------------------------------------------
# echo 934840 > C:\AutomatedBuilds\C27\Capstone\ThinkArcade\Build_Dir\WindowsNoEditor\FrostRunner\Binaries\Win64\steam_appid.txt