@echo off

set base_dir=C:\AutomatedBuilds\C28\TGP3\Tex_Mechs\
set executable_dir=%base_dir%Executable\
set executable_build_script="%executable_dir%Executable_Build_Script.iss"
set archive_dir=%base_dir%Archived_Builds\

set network_dir=smu.edu\files\Guildhall$\Deleted Nightly\C28_Capstone\Tex-Mechs\Executable
set smu_username=SMU\spn02745
set smu_password=W3bu1ldg@m35

set build_month=%date:~4,2%
set build_day=%date:~7,2%
set build_hour=%time:~0,2%
set build_minute=%time:~3,2%
if %build_hour% lss 10 set hour=0%build_hour:~1,2%

set output_executable_file=TexMechs_Auto_%build_month%_%build_day%_%build_hour%_%build_minute%.exe
set initial_executable_file=Tex-Mechs.exe


rem Step 4 - We have the time stamped installer, all that remains now is to get it in our archive of installers and on the network drive
echo ----------------------------------------------------------------------
echo Step 4: Copying installer executable to archive directory and network drive
echo ----------------------------------------------------------------------


rem Here you want to list your SMU username and password - again, might be good to get an account to use, but I just used mine
rem PERSISTENT here means do we want to remember this mapping, I always defaulted to NO
net use F: \\%network_dir%\ /user:%smu_username% %smu_password% /persistent:no /savecred


rem Copy to the archive
rem echo Copying installer
rem echo  from %executable_dir%%initial_executable_file%
rem echo  to   %archive_dir% as %output_executable_file%
copy %executable_dir%%initial_executable_file% "%archive_dir%"
ren %archive_dir%%initial_executable_file% %output_executable_file%

rem Move to the network drive
rem echo Moving installer
rem echo  from %executable_dir%%initial_executable_file%
rem echo  to   %network_dir% as %output_executable_file%
copy %archive_dir%%output_executable_file% "\\%network_dir%\"

echo:
echo:


rem Step 5 - Unmap the network drive, we don't need it anymore
echo ----------------------------------------------------------------------
echo Step 5: Remove the network drive mapping
echo ----------------------------------------------------------------------


echo Unmapping network drive %network_dir%
net use F: /d


rem Go to end of file, where we're done! Success! (this goes around the fail case)

rem Fail case - the build is broken
rem This was my way of being more explicit with broken builds - it just creates an empty text file with the name BUILD_BROKEN.txt, so anyone on your
rem team can recognize when it's broken.

rem Potential use case here - get the build output log from above that you could make, and copy it here with the BUILD_BROKEN name, then anyone can
rem parse it to find the error.